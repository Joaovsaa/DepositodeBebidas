from django.db import models
from django.db.models import Sum

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    class Meta:
    	verbose_name_plural = "Clientes"

    def __str__(self):
    	return self.nome

class Produto(models.Model):
    CATEGORIA_CHOICES = [
        ('bebidas', 'Bebidas'),
        ('alimentos', 'Alimentos'),
        ('kits', 'Kits'),
        ('utensílios', 'Utensílios')
    ]
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)

    class Meta:
    	verbose_name_plural = "Produtos"

    def __str__(self):
    	return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='VendaProduto')
    data = models.DateTimeField(auto_now_add=True)


class VendaProduto(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produtos_para_venda = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_vendida = models.PositiveIntegerField()

    class Meta:
    	verbose_name_plural = "Realizar Vendas"