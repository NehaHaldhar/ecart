# Generated by Django 4.2 on 2023-05-10 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_remove_buyer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
