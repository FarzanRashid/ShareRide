# Generated by Django 5.0.4 on 2024-05-08 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestride', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='user_id',
            new_name='user',
        ),
    ]
