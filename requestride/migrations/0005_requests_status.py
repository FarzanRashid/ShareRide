# Generated by Django 5.0.4 on 2024-05-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestride', '0004_rename_user_id_requests_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
