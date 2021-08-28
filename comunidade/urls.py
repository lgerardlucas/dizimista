from django.urls import path
from .views import listar_comunidades, adicionar_comunidade, alterar_comunidade, deletar_comunidade

app_name = 'comunidade'

urlpatterns = [
    path('listar/', listar_comunidades, name='listar_comunidades'),
    path('adicionar/', adicionar_comunidade, name='adicionar_comunidade'),
    path('deletar/<int:id>', deletar_comunidade, name='deletar_comunidade'),
    path('alterar/<int:id>', alterar_comunidade, name='alterar_comunidade'),

]
