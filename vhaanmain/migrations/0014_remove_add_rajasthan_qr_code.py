# Generated by Django 5.0.1 on 2024-03-08 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0013_add_rajasthan_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_rajasthan',
            name='qr_code',
        ),
    ]
