# Generated by Django 5.0.1 on 2024-07-12 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0048_rename_user_name_stateassign_admin_custom_admin_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stateassign_admin_custom',
            name='admin_name',
        ),
        migrations.RemoveField(
            model_name='stateassign_admin_custom',
            name='state_name',
        ),
        migrations.DeleteModel(
            name='admin_list',
        ),
        migrations.DeleteModel(
            name='stateAssign_admin_custom',
        ),
    ]