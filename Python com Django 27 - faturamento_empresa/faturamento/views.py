from django.shortcuts import render, get_object_or_404, redirect
from .models import Faturamento
from .forms import FaturamentoForm
import matplotlib.pyplot as plt
import io
import urllib, base64
import json

def listar_faturamento(request):
    faturamentos = Faturamento.objects.all()
    return render(request, 'faturamento/lista.html', {'faturamentos': faturamentos})

def criar_faturamento(request):
    if request.method == "POST":
        form = FaturamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_faturamento')
    else:
        form = FaturamentoForm()
    return render(request, 'faturamento/form.html', {'form': form})

def editar_faturamento(request, id):
    faturamento = get_object_or_404(Faturamento, id=id)
    if request.method == "POST":
        form = FaturamentoForm(request.POST, instance=faturamento)
        if form.is_valid():
            form.save()
            return redirect('listar_faturamento')
    else:
        form = FaturamentoForm(instance=faturamento)
    return render(request, 'faturamento/form.html', {'form': form})

def excluir_faturamento(request, id):
    faturamento = get_object_or_404(Faturamento, id=id)
    if request.method == "POST":
        faturamento.delete()
        return redirect('listar_faturamento')
    return render(request, 'faturamento/confirmar_exclusao.html', {'faturamento': faturamento})

def visualizar_grafico(request, id):
    faturamento = get_object_or_404(Faturamento, id=id)

    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    valores = [
        float(faturamento.janeiro), float(faturamento.fevereiro), float(faturamento.marco),
        float(faturamento.abril), float(faturamento.maio), float(faturamento.junho),
        float(faturamento.julho), float(faturamento.agosto), float(faturamento.setembro),
        float(faturamento.outubro), float(faturamento.novembro), float(faturamento.dezembro)
    ]

    dados_grafico = json.dumps({'meses': meses, 'valores': valores})

    return render(request, 'faturamento/grafico.html', {'dados_grafico': dados_grafico, 'faturamento': faturamento})
