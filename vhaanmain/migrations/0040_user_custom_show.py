# Generated by Django 5.0.1 on 2024-07-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0039_add_haryana_recipt_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_custom',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]