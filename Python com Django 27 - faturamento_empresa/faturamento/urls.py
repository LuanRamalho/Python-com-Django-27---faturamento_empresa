from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_faturamento, name='listar_faturamento'),
    path('novo/', views.criar_faturamento, name='criar_faturamento'),
    path('editar/<int:id>/', views.editar_faturamento, name='editar_faturamento'),
    path('excluir/<int:id>/', views.excluir_faturamento, name='excluir_faturamento'),
    path('grafico/<int:id>/', views.visualizar_grafico, name='visualizar_grafico'),
]
