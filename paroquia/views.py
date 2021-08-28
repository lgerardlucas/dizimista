from django.shortcuts import render, redirect, get_object_or_404
from .models import Paroquia
from .forms import ParoquiaForm
from django.db import IntegrityError
from django.contrib import messages
from utils import normalize

app_name = 'paroquia'

def listar_paroquias(request):
    template_name = 'listar_paroquias.html'
    paroquias = Paroquia.objects.all()
    context = {
        'title_scope':'Paróquia - Listar',
        'records': paroquias,
    }
    return render(request, template_name, context)

def adicionar_paroquia(request):
    template_name = 'adicionar_paroquia.html'
    form = ParoquiaForm(request.POST or None)
    if form.is_valid():
        try:
            paroquia = form.save(commit=False)
            paroquia.name = request.POST.get('nome')
            paroquia.save()
        except IntegrityError as e:
            if 'UNIQUE' in str(e).upper():
                messages.add_message(request, messages.INFO, '"'+paroquia.name+'" já cadastrada!')
            else:
                messages.add_message(request, messages.INFO, 'Erro ao incluir a "'+paroquia.name+'! '+str(e))
            return redirect('paroquia:adicionar_paroquia')
        return redirect('paroquia:listar_paroquias')
    else:
        messages.add_message(request, messages.INFO, form.errors)

    context = {
        'title_scope':'Paróquia - Adicionar',
        'records':form,
    }
    return render(request, template_name, context)

def deletar_paroquia(request, id):
    paroquia = Paroquia.objects.filter(id=id)
    if paroquia:
        paroquia.delete()
    return redirect('paroquia:listar_paroquias')

def alterar_paroquia(request):
    pass
