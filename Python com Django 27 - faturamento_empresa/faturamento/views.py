from django.shortcuts import render, get_object_or_404, redirect
from .models import Faturamento
from .forms import FaturamentoForm
import matplotlib.pyplot as plt
import io
import urllib, base64

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

    # Converter valores Decimal para float
    valores = [
        float(faturamento.janeiro), float(faturamento.fevereiro), float(faturamento.marco),
        float(faturamento.abril), float(faturamento.maio), float(faturamento.junho),
        float(faturamento.julho), float(faturamento.agosto), float(faturamento.setembro),
        float(faturamento.outubro), float(faturamento.novembro), float(faturamento.dezembro)
    ]

    plt.figure(figsize=(10, 5))
    barras = plt.bar(meses, valores, color='blue')

    # Exibir os valores no topo de cada barra
    for barra, valor in zip(barras, valores):
        plt.text(barra.get_x() + barra.get_width() / 2, valor + 0.5, f"R$ {valor:.2f}",
                 ha='center', va='bottom', fontsize=10, color="black", fontweight="bold")

    plt.xlabel("Meses")
    plt.ylabel("Faturamento (R$)")
    plt.title(f"Faturamento de {faturamento.ano}")
    plt.ylim(0, max(valores) * 1.2)  # Ajusta a altura para não cortar os valores

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagem_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()

    return render(request, 'faturamento/grafico.html', {'imagem_base64': imagem_base64, 'faturamento': faturamento})
