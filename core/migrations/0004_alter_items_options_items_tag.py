# Generated by Django 4.1.2 on 2022-11-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_items_formula_1_items_formula_2_items_formula_3_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='items',
            name='tag',
            field=models.SlugField(default='lorem', max_length=20),
            preserve_default=False,
        ),
    ]