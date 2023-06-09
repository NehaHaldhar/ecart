# Generated by Django 4.2 on 2023-05-20 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0020_alter_buyer_addressline1_alter_buyer_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('paymentMode', models.IntegerField(choices=[(1, 'Cash on Delivery'), (2, 'Net Banking')], default=1)),
                ('paymentStatus', models.IntegerField(choices=[(1, 'Pending'), (2, 'Done')], default=1)),
                ('orderStatus', models.IntegerField(choices=[(1, 'Order Placed'), (2, 'Ready To Dispatch'), (3, 'Dispatched'), (4, 'Out For Delivery'), (5, 'Delivered')], default=1)),
                ('subtotal', models.IntegerField()),
                ('shipping', models.IntegerField()),
                ('final', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('orderDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.orderdetails')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
            ],
        ),
    ]
