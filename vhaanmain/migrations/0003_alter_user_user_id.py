# Generated by Django 5.0.1 on 2024-03-06 05:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0002_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=uuid.uuid4, max_length=20),
        ),
    ]