from . import models
from django_filters import FilterSet 
from django_filters.filters import CharFilter, ModelChoiceFilter, ChoiceFilter


class CategoriaFilterSet(FilterSet):
    nome = CharFilter(method='nome_filter', )

    class Meta:
        model = models.Categoria
        fields = {}

    def __init__(self, data, *args, **kwargs):
        data = data.copy()
        data.setdefault('data', '-data')
        super().__init__(data, *args, **kwargs)

        self.filters['nome'].field.widget.attrs.update({
            'class': 'form-control col-lg-12', 
            'placeholder': 'Buscar categoria',
            'style': 'height: 100%;',    
        })

    def nome_filter(self, queryset, name, value):
        return queryset.filter(nome__icontains=value)


class ProdutoFilterSet(FilterSet):
    preco = ChoiceFilter(
        choices=[
            ('preco', 'Menor Preço'),
            ('-preco', 'Maior Preço'),
        ],
        method='preco_filter',
    )
    
    categoria = ModelChoiceFilter(
        method='categoria_filter',
        queryset=models.Categoria.objects.all(),
    )

    busca = CharFilter(method='busca_filter', )

    class Meta:
        model = models.Produto
        fields = {}

    def __init__(self, data, *args, **kwargs):
        data = data.copy()
        data.setdefault('data', '-data')
        super().__init__(data, *args, **kwargs)
    
        self.filters['categoria'].field.widget.attrs.update({
            'class': 'form-control',
        })
        
        self.filters['preco'].field.widget.attrs.update({
            'class': 'form-control',
        })

        self.filters['busca'].field.widget.attrs.update({
            'class': 'form-control h-100',
            'placeholder': 'Buscar Produto',
        })

    def categoria_filter(self, queryset, name, value):
        return queryset.filter(categoria=value)

    def preco_filter(self, queryset, name, value):
        return queryset.order_by(value)

    def busca_filter(self, queryset, name, value):
        return queryset.filter(nome__icontains=value)
