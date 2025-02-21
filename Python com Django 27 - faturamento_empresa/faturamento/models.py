from django.db import models

class Faturamento(models.Model):
    ano = models.IntegerField()
    janeiro = models.DecimalField(max_digits=10, decimal_places=2)
    fevereiro = models.DecimalField(max_digits=10, decimal_places=2)
    marco = models.DecimalField(max_digits=10, decimal_places=2)
    abril = models.DecimalField(max_digits=10, decimal_places=2)
    maio = models.DecimalField(max_digits=10, decimal_places=2)
    junho = models.DecimalField(max_digits=10, decimal_places=2)
    julho = models.DecimalField(max_digits=10, decimal_places=2)
    agosto = models.DecimalField(max_digits=10, decimal_places=2)
    setembro = models.DecimalField(max_digits=10, decimal_places=2)
    outubro = models.DecimalField(max_digits=10, decimal_places=2)
    novembro = models.DecimalField(max_digits=10, decimal_places=2)
    dezembro = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Faturamento {self.ano}"
