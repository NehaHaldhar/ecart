# Generated by Django 4.2 on 2023-05-20 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0022_alter_orderedproducts_qty_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderDetails',
            new_name='OrderDetail',
        ),
        migrations.RenameModel(
            old_name='OrderedProducts',
            new_name='OrderedProduct',
        ),
    ]
