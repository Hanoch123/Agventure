# Generated by Django 3.2.7 on 2021-11-20 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
    ]
