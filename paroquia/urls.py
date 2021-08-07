from django.urls import path
from .views import listar_paroquias, adicionar_paroquia, alterar_paroquia, deletar_paroquia

app_name = 'paroquia'

urlpatterns = [
    path('listar/', listar_paroquias, name='listar_paroquias'),
    path('adicionar/', adicionar_paroquia, name='adicionar_paroquia'),
    path('deletar/<int:id>', deletar_paroquia, name='deletar_paroquia'),
    path('alterar/<int:id>', alterar_paroquia, name='alterar_paroquia'),

]