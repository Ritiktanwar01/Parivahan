# Generated by Django 5.0.1 on 2024-03-06 04:46

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='statelists',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default=uuid.uuid4, editable=False, max_length=20)),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='stateassigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vhaanmain.users')),
            ],
        ),
    ]