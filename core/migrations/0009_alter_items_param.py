# Generated by Django 4.1.2 on 2022-11-16 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_items_param'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Param',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
