# Generated by Django 5.0.1 on 2024-03-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0019_alter_add_haryana_servicetype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_haryana',
            name='create_date',
            field=models.CharField(max_length=80, null=True),
        ),
    ]