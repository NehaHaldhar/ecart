# Generated by Django 4.2 on 2023-05-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_brand_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('addressline1', models.CharField(max_length=100)),
                ('addressline2', models.CharField(max_length=100)),
                ('addressline3', models.CharField(max_length=100)),
                ('pin', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pic', models.ImageField(upload_to='buyers')),
            ],
        ),
    ]
