# Generated by Django 4.1.2 on 2022-11-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_items_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='Formula_8',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]
