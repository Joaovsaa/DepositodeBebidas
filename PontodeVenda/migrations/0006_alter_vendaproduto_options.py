# Generated by Django 4.2 on 2023-05-03 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PontodeVenda', '0005_alter_vendaproduto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendaproduto',
            options={'verbose_name': 'Produto ao Carrinho', 'verbose_name_plural': 'Carrinho'},
        ),
    ]
