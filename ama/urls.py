from . import views
from django.urls import path


app_name = 'ama'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('sobre/', views.Sobre.as_view(), name='sobre'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('doacao/', views.Doacao.as_view(), name='doacao'),

    # Mensagem
    path('contato/', views.Mensagem.as_view(), name='contato'),
    path('mensagens', views.ListarMensagens.as_view(), name='mensagens'),
    path('detalhes_mensagem/<int:pk>', views.DetalhesMensagem.as_view(), name='detalhes_mensagem'),
    path('excluir_mensagem/<int:pk>', views.excluir_mensagem, name='excluir_mensagem'),
    path('marcar_lida/<int:pk>', views.marcar_lida, name='marcar_lida'),

    # Noticia
    path('escrever_noticia/', views.EscreverNoticia.as_view(), name='escrever_noticia'),
    path('editar_noticia/<slug>', views.EditarNoticia.as_view(), name='editar_noticia'),
    path('excluir_noticia/<int:pk>', views.excluir_noticia, name='excluir_noticia'),
    path('detalhes_noticia/<slug>', views.DetalhesNoticia.as_view(), name='detalhes_noticia'),
    path('listar_noticias/', view=views.ListarNoticias.as_view(), name='listar_noticias'),

    # Parceiro
    path('adicionar_parceiro/', views.AdicionarParceiro.as_view(), name='adicionar_parceiro'),
    path('editar_parceiro/<int:pk>', views.EditarParceiro.as_view(), name='editar_parceiro'),
    path('excluir_parceiro/<int:pk>', views.excluir_parceiro, name='excluir_parceiro'),
    path('parceiros', views.ListarParceiros.as_view(), name='parceiros'),
]
