from django.contrib import admin
from .models import Produto, Cliente, Venda, VendaProduto
from django.db.models import Sum, F


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nome',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'endereco')
    search_fields = ('nome',)


class VendaProdutoInline(admin.TabularInline):
    model = VendaProduto
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    inlines = (VendaProdutoInline,)
    list_display = ('cliente', 'data', 'total')
    search_fields = ('cliente__nome',)
    
    def total(self, obj):
        return sum(vp.quantidade_vendida * vp.produtos_para_venda.valor for vp in obj.produtos.all())
    total.short_description = 'Total'

admin.site.register(Venda, VendaAdmin)
       