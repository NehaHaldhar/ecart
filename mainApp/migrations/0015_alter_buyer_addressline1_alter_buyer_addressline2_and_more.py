# Generated by Django 4.2 on 2023-05-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0014_buyer_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='addressline1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='addressline2',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='addressline3',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
