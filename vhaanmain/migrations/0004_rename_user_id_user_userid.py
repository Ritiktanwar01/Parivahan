# Generated by Django 5.0.1 on 2024-03-06 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0003_alter_user_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='userid',
        ),
    ]
