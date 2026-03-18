from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'meuapp/list.html', {'pessoas': pessoas})

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'meuapp/form.html', {'form': form})

# Create your views here.
