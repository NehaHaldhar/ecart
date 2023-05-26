# Generated by Django 4.2 on 2023-05-19 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0019_alter_buyer_addressline1_alter_buyer_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='addressline1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='city',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='pin',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='state',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
