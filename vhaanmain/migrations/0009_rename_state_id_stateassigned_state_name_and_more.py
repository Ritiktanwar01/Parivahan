# Generated by Django 5.0.1 on 2024-03-06 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0008_remove_user_userid_alter_stateassigned_state_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stateassigned',
            old_name='state_id',
            new_name='state_name',
        ),
        migrations.RenameField(
            model_name='stateassigned',
            old_name='user_id',
            new_name='user_name',
        ),
    ]
