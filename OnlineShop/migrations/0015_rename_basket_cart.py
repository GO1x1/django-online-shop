# Generated by Django 4.2 on 2023-04-25 15:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OnlineShop', '0014_basket'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Basket',
            new_name='Cart',
        ),
    ]