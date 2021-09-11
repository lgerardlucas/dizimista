from django.shortcuts import render, redirect, get_object_or_404
from .models import Ofertante
from .forms import OfertanteForm
from django.db import IntegrityError
from django.contrib import messages
from utils import normalize
from comunidade.models import Comunidade

app_name = 'ofertante'

def listar_ofertantes(request):
    template_name = 'listar_ofertantes.html'
    ofertante = Ofertante.objects.all().order_by('name')
    context = {
        'title_scope':'Dizimista - Listar',
        'records': ofertante,
    }
    return render(request, template_name, context)

def adicionar_ofertante(request):
    template_name = 'adicionar_ofertante.html'
    form = OfertanteForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                ofertante = form.save(commit=False)
                ofertante.name = request.POST.get('name')
                ofertante.comunidade = Comunidade.objects.all().first() #Apenas uma paroquia por enquanto!
                ofertante.save()
            except IntegrityError as e:
                if 'UNIQUE' in str(e).upper():
                    messages.add_message(request, messages.INFO, '"'+ofertante.name+'" já cadastrada!')
                else:
                    messages.add_message(request, messages.INFO, 'Erro ao incluir a "'+ofertante.name+'! '+str(e))
                return redirect('ofertante:adicionar_ofertante')
            return redirect('ofertante:listar_ofertantes')
        else:
            messages.add_message(request, messages.INFO, form.errors)
    else:
        form = OfertanteForm()
    context = {
        'title_scope':'Dizimista - Adicionar',
        'record':form,
        'type_acess': 'add',
    }
    return render(request, template_name, context)

def alterar_ofertante(request, id):
    template_name = 'adicionar_ofertante.html'
    ofertante = Ofertante.objects.get(id=id)
    if request.method == 'POST':
        form = OfertanteForm(request.POST or None, instance=ofertante)
        if form.is_valid():
            try:
                ofertante = form.save(commit=False)
                ofertante.name = request.POST.get('name')
                ofertante.comunidade = Comunidade.objects.all().first() #Apenas uma comunidade por enquanto!
                ofertante.save()
            except IntegrityError as e:
                if 'UNIQUE' in str(e).upper():
                    messages.add_message(request, messages.INFO, '"'+ofertante.name+'" já cadastrada!')
                else:
                    messages.add_message(request, messages.INFO, 'Erro ao incluir a "'+ofertante.name+'! '+str(e))
                return redirect('ofertante:adicionar_ofertante')
            return redirect('ofertante:listar_ofertantes')
        else:
            messages.add_message(request, messages.INFO, form.errors)
    else:
        form = ofertante
    context = {
        'title_scope':'Dizimista - Alterar',
        'record': form,
        'type_acess': 'alt',
    }
    return render(request, template_name, context)


def deletar_ofertante(request, id):
    ofertante = Ofertante.objects.filter(id=id)
    if ofertante:
        ofertante.delete()
    return redirect('ofertante:listar_ofertantes')
