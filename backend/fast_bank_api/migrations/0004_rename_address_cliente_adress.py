# Generated by Django 4.1 on 2022-09-28 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fast_bank_api', '0003_alter_cartao_client_alter_cliente_account_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='address',
            new_name='adress',
        ),
    ]
