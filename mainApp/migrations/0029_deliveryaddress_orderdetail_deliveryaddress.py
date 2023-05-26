# Generated by Django 4.2 on 2023-05-24 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0028_alter_subcategory_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receiver_name', models.CharField(max_length=40)),
                ('contact', models.CharField(max_length=15)),
                ('pincode', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=60)),
                ('locality_town', models.CharField(max_length=20)),
                ('city_district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='deliveryAddress',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainApp.deliveryaddress'),
        ),
    ]