# Generated by Django 4.1.2 on 2022-11-16 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_items_options_items_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'ordering': ['tag']},
        ),
    ]