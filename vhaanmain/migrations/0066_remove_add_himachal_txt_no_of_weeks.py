# Generated by Django 5.0.1 on 2024-07-13 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0065_remove_add_himachal_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_himachal',
            name='txt_no_of_weeks',
        ),
    ]