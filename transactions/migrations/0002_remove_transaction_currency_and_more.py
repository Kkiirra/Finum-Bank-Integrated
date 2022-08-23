# Generated by Django 4.0 on 2022-08-15 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0001_initial'),
        ('orders', '0003_alter_order_contractor'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='currency',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='contractor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contractors.contractor'),
        ),
        migrations.DeleteModel(
            name='Contractor',
        ),
    ]
