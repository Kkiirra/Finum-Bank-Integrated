# Generated by Django 4.0 on 2022-10-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0014_alter_invoiceitem_price'),
        ('transactions', '0014_alter_transaction_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='invoice',
            field=models.ManyToManyField(blank=True, related_name='transactions', to='invoice.Invoice'),
        ),
    ]