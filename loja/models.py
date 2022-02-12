from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class ProdutoFoto(models.Model):
    foto = models.ImageField(upload_to='produto/')

    class Meta:
        verbose_name = 'Produto Foto'
        verbose_name_plural = 'Produtos Fotos'

    def __str__(self):
        return self.foto.url


class Produto(models.Model):
    nome = models.CharField(max_length= 255)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(
        decimal_places=2, 
        max_digits=5,
    )
    preco_promocional = models.DecimalField(
        decimal_places=2, 
        max_digits=5, 
        blank=True, 
        null=True
    )
    descricao = models.TextField()
    fotos = models.ManyToManyField(ProdutoFoto, verbose_name='Fotos')

    def __str__(self):
        return self.nome

    def get_discount_percentage(self):
        result = 100 - (self.preco_promocional * 100 / self.preco)
        return round(result, 0)
    