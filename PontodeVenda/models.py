from django.db import models


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
    quantidade = models.PositiveIntegerField()
    descricao = models.TextField(verbose_name="Descrição",max_length = 500, blank = True, null = True)

    class Meta:
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    # Total é um Field calculado, não armazenado no BD

    class Meta:
        verbose_name_plural = "Vendas"

    def __str__(self):
        return self.data.strftime("%H: %M %d/%m/%Y")


class VendaProduto(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"

    def save(self, *args, **kwargs):
        super(VendaProduto, self).save(*args, **kwargs)
        self.produto.quantidade -= self.quantidade
        self.produto.save()

    def delete(self, *args, **kwargs):
        self.produto.quantidade += self.quantidade
        self.produto.save()
        super(VendaProduto, self).delete(*args, **kwargs)

    @property
    def valor_total(self):
        return self.quantidade * self.produto.valor

    class Meta:
        verbose_name_plural = "Carrinho"
        verbose_name = "Produto ao Carrinho"