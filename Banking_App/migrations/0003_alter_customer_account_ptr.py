# Generated by Django 4.2.7 on 2024-02-12 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Banking_App', '0002_remove_customer_customer_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='account_ptr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Banking_App.account'),
        ),
    ]