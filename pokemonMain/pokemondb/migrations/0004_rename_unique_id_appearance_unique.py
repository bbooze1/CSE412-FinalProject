# Generated by Django 3.2.9 on 2021-11-29 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemondb', '0003_auto_20211129_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appearance',
            old_name='unique_id',
            new_name='unique',
        ),
    ]
