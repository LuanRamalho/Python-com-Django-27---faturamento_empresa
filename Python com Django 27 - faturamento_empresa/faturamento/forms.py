from django import forms
from .models import Faturamento

class FaturamentoForm(forms.ModelForm):
    class Meta:
        model = Faturamento
        fields = '__all__'
