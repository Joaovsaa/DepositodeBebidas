# Generated by Django 4.2 on 2023-05-03 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PontodeVenda', '0004_alter_venda_options_alter_vendaproduto_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendaproduto',
            options={'verbose_name': 'Realizar Venda', 'verbose_name_plural': 'Realizar Vendas'},
        ),
    ]
