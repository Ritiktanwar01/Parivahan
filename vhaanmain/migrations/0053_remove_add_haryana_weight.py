# Generated by Django 5.0.1 on 2024-07-13 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0052_add_uttarpradesh_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_haryana',
            name='Weight',
        ),
    ]