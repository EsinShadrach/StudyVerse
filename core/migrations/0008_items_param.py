# Generated by Django 4.1.2 on 2022-11-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_items_formula_8'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='Param',
            field=models.TextField(blank=True, max_length=40, null=True),
        ),
    ]
