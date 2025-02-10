# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, default=0)
    category_name = models.CharField(max_length=100)

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=300)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_uploaddate = models.DateField(auto_now_add=True)
    product_image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    totalprice = models.DecimalField(max_digits=10, decimal_places=2)
    totalcartprice=models.DecimalField(max_digits=12,decimal_places=2,default=0.00)



