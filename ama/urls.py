from os import name
from . import views
from django.urls import path


app_name = 'ama'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('sobre/', views.Sobre.as_view(), name='sobre'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('contato/', views.Mensagem.as_view(), name='contato'),

    # Noticia
    path('escrever_noticia/', views.EscreverNoticia.as_view(),
         name='escrever_noticia'),
    # TODO: Alterar id para slug na url de editar notícia
    path('editar_noticia/<int:pk>', views.EditarNoticia.as_view(),
         name='editar_noticia'),
    path('detalhes_noticia/<slug>', views.DetalhesNoticia.as_view(),
         name='detalhes_noticia'),
    path('listar_noticias/', view=views.ListarNoticias.as_view(),
         name='listar_noticias'),

    # Parceiro
    path('adicionar_parceiro/', views.AdicionarParceiro.as_view(),
         name='adicionar_parceiro'),
    path('editar_parceiro/<int:pk>', views.EditarParceiro.as_view(),
         name='editar_parceiro'),
    path('excluir_parceiro/<int:pk>',
         views.excluir_parceiro, name='excluir_parceiro'),
]
