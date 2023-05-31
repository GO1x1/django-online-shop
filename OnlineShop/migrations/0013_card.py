# Generated by Django 4.2 on 2023-04-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineShop', '0012_alter_product_photo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=20)),
                ('cvc', models.CharField(max_length=3)),
                ('month', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=2)),
            ],
        ),
    ]
