# Generated by Django 4.2 on 2023-04-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineShop', '0021_alter_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_f',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
