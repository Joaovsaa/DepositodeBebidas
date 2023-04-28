from django.contrib import admin
from .models import Cliente, Produto, Venda, VendaProduto

class ProdutoInline(admin.TabularInline):
    model = VendaProduto
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'quantidade', 'categoria')
    list_filter = ('categoria',)
    search_filter = ('nome',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'endereco')
    search_filter = ('nome', 'contato',)

class VendaAdmin(admin.ModelAdmin):
    inlines = [ProdutoInline,]
    list_display = ('cliente', 'data', 'total_venda')

    def total_venda(self, obj):
        total = 0
        for venda_produto in obj.vendaproduto_set.all():
            total += venda_produto.quantidade * venda_produto.produto.valor
        return f'R$ {total:.2f}'

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)


