# Generated by Django 4.0 on 2022-08-15 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_remove_transaction_currency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='company',
        ),
    ]
