# Generated by Django 5.0.1 on 2024-07-10 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0038_add_uttarpradesh_recipt_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_haryana',
            name='recipt_no',
            field=models.CharField(default='default', max_length=80),
        ),
    ]