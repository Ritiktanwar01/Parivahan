# Generated by Django 5.0.1 on 2024-07-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhaanmain', '0056_add_maharashtra_recipt_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_gujrat',
            name='total_amt_text',
            field=models.CharField(default='none', max_length=80),
        ),
    ]