# Generated by Django 4.2 on 2023-05-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='pin',
            field=models.CharField(max_length=10),
        ),
    ]