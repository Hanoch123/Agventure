# Generated by Django 3.2.7 on 2021-11-23 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_customer_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Seller',
        ),
    ]