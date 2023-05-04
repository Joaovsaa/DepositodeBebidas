from django.contrib import admin
from .models import Cliente, Produto, Venda, VendaProduto
from import_export.admin import ExportMixin, ImportMixin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.formats import base_formats


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


class RelatorioVendaResource(resources.ModelResource):
    cliente_nome = fields.Field(attribute='cliente__nome', column_name='Nome do Cliente')
    venda_data = fields.Field(attribute='data', column_name='Data da Venda')
    produtos = fields.Field(column_name='Produtos')
    quantidades = fields.Field(column_name='Quantidades')
    valores = fields.Field(column_name='Valores')
    total = fields.Field(column_name='Total da Venda')

    class Meta:
        model = VendaProduto
        fields = ('cliente_nome', 'venda_data', 'produtos', 'quantidades', 'valores', 'total')
        export_order = ('cliente_nome', 'venda_data', 'produtos', 'quantidades', 'valores', 'total')
        import_id_fields = ['cliente_nome', 'venda_data', 'produtos']
        skip_unchanged = True
        report_skipped = False

    def dehydrate_produtos(self, venda):
        return ','.join([vp.produto.nome for vp in venda.vendaproduto_set.all()])

    def dehydrate_quantidades(self, venda):
        return ','.join([str(vp.quantidade) for vp in venda.vendaproduto_set.all()])

    def dehydrate_valores(self, venda):
        return ','.join([f'R$ {vp.produto.valor:.2f}' for vp in venda.vendaproduto_set.all()])

    def dehydrate_total(self, venda):
        total = 0
        for vp in venda.vendaproduto_set.all():
            total += vp.produto.valor * vp.quantidade
        return f'R$ {total:.2f}'

class VendaAdmin(ExportMixin, ImportMixin, admin.ModelAdmin):
    inlines = [ProdutoInline, ]
    list_display = ('cliente', 'data', 'total_venda')
    
    search_fields = ('cliente__nome', 'vendaproduto__produto__nome')

    def total_venda(self, obj):
        total = 0
        for venda_produto in obj.vendaproduto_set.all():
            total += venda_produto.quantidade * venda_produto.produto.valor
        return f'R$ {total:.2f}'

    # Add export functionality from RelatorioVendaResource
    resource_class = RelatorioVendaResource
    formats = [base_formats.CSV, base_formats.XLSX, base_formats.TSV, base_formats.ODS]
    export_order = ('cliente_nome', 'venda_data', 'produtos', 'quantidades', 'valores', 'total')


# Register the models
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)
