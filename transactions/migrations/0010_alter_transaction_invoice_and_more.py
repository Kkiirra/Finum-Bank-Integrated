# Generated by Django 4.0 on 2022-10-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0006_alter_user_account_default_currency_and_more'),
        ('invoice', '0006_alter_invoice_invoice_name_and_more'),
        ('transactions', '0009_transaction_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='invoice',
            field=models.ManyToManyField(blank=True, to='invoice.Invoice'),
        ),
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together={('transaction_id', 'user_account')},
        ),
    ]