# Generated by Django 5.0.1 on 2024-12-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_shoppingcart_totalcartprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
