# Generated by Django 4.0.5 on 2022-06-29 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='guest_can_pausa',
            new_name='guest_can_pause',
        ),
    ]
