# Generated by Django 5.0.1 on 2024-07-12 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0046_alter_stateassigned_state_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='stateAssign_admin_custom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vhaanmain.statelists')),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vhaanmain.admin_list')),
            ],
        ),
    ]
