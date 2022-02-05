from . import models
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome')
    list_display_links = ('pk', 'nome')


admin.site.register(models.Categoria, CategoriaAdmin)


class ProdutoFotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'foto')
    list_display_links = ('pk', 'foto')


admin.site.register(models.ProdutoFoto, ProdutoFotoAdmin)


class ProdutoFotoInline(admin.TabularInline):
    model = models.Produto.fotos.through
    extra = 0


class ProdutoAdmin(SummernoteModelAdmin):
    list_display = ('pk', 'nome', 'quantidade', 'preco', 'preco_promocional', 'categoria')
    list_display_links = ('pk', 'nome', 'quantidade', 'preco', 'preco_promocional', 'categoria')

    summernote_fields = ['descricao']

    exclude=['fotos']
    inlines = [ProdutoFotoInline]


admin.site.register(models.Produto, ProdutoAdmin)
