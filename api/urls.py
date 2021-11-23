from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('criar_especialidade/', views.criar_especialidade, name='criar_especialidade'),
    path('editar_especialidade/<int:pk>/', views.editar_especialidade, name='editar_especialidade'),
    path('listar_especialidade/', views.listar_especialidade, name='listar_especialidade'),
    path('deletar_especialidade/<int:pk>/', views.deletar_especialidade, name='deletar_especialidade'),
    path('criar_medico/', views.criar_medico, name='criar_medico'),
    path('editar_medico/<int:pk>/', views.editar_medico, name='editar_medico'),
    path('listar_medico/', views.listar_medico, name='listar_medico'),
    path('deletar_medico/<int:pk>/', views.deletar_medico, name='deletar_medico'),
    path('criar_consulta/', views.criar_consulta, name='criar_consulta'),
    path('editar_consulta/<int:pk>/', views.editar_consulta, name='editar_consulta'),
    path('listar_consulta/', views.listar_consulta, name='listar_consulta'),
    path('deletar_consulta/<int:pk>/', views.deletar_consulta, name='deletar_consulta'),

]