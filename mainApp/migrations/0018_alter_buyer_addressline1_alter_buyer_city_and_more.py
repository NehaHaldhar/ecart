# Generated by Django 4.2 on 2023-05-19 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0017_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='addressline1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='pin',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='state',
            field=models.CharField(default='', max_length=30),
        ),
    ]
