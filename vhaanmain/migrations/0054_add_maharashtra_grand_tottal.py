# Generated by Django 5.0.1 on 2024-07-13 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0053_remove_add_haryana_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_maharashtra',
            name='grand_tottal',
            field=models.IntegerField(default=0),
        ),
    ]