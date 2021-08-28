from django.shortcuts import render, redirect, get_object_or_404
from .models import Comunidade
from .forms import ComunidadeForm
from django.db import IntegrityError
from django.contrib import messages
from utils import normalize

app_name = 'comunidade'

def listar_comunidades(request):
    template_name = 'listar_comunidades.html'
    comunidade = Comunidade.objects.all()
    context = {
        'title_scope':'Comunidade - Listar',
        'records': comunidade,
    }
    return render(request, template_name, context)

def adicionar_comunidade(request):
    template_name = 'adicionar_comunidade.html'
    form = ComunidadeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                comunidade = form.save(commit=False)
                comunidade.name = request.POST.get('name')
                comunidade.save()
            except IntegrityError as e:
                if 'UNIQUE' in str(e).upper():
                    messages.add_message(request, messages.INFO, '"'+comunidade.name+'" já cadastrada!')
                else:
                    messages.add_message(request, messages.INFO, 'Erro ao incluir a "'+comunidade.name+'! '+str(e))
                return redirect('comunidade:adicionar_comunidade')
            return redirect('comunidade:listar_comunidades')
        else:
            messages.add_message(request, messages.INFO, form.errors)
    else:
        form = ComunidadeForm()
    context = {
        'title_scope':'Comunidade - Adicionar',
        'record':form,
        'type_acess': 'add',
    }
    return render(request, template_name, context)

def alterar_comunidade(request, id):
    template_name = 'adicionar_comunidade.html'
    comunidade = Comunidade.objects.get(id=id)
    if request.method == 'POST':
        form = ComunidadeForm(request.POST or None, instance=comunidade)
        if form.is_valid():
            try:
                comunidade = form.save(commit=False)
                comunidade.name = request.POST.get('name')
                comunidade.save()
            except IntegrityError as e:
                if 'UNIQUE' in str(e).upper():
                    messages.add_message(request, messages.INFO, '"'+comunidade.name+'" já cadastrada!')
                else:
                    messages.add_message(request, messages.INFO, 'Erro ao incluir a "'+comunidade.name+'! '+str(e))
                return redirect('comunidade:adicionar_comunidade')
            return redirect('comunidade:listar_comunidades')
        else:
            messages.add_message(request, messages.INFO, form.errors)
    else:
        form = comunidade
    context = {
        'title_scope':'Comunidade - Alterar',
        'record': form,
        'type_acess': 'alt',
    }
    return render(request, template_name, context)


def deletar_comunidade(request, id):
    comunidade = Comunidade.objects.filter(id=id)
    if comunidade:
        comunidade.delete()
    return redirect('comunidade:listar_comunidades')
