from django.urls import path
from .views import listar_ofertantes, adicionar_ofertante, alterar_ofertante, deletar_ofertante

app_name = 'ofertante'

urlpatterns = [
    path('listar/', listar_ofertantes, name='listar_ofertantes'),
    path('adicionar/', adicionar_ofertante, name='adicionar_ofertante'),
    path('deletar/<int:id>', deletar_ofertante, name='deletar_ofertante'),
    path('alterar/<int:id>', alterar_ofertante, name='alterar_ofertante'),
]
