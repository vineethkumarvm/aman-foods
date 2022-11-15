from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name



class Product(models.Model):
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    product_name= models.CharField(max_length=200)
    product_image = models.ImageField()
    price = models.IntegerField()
    quantity = models.CharField(max_length=10)
    
    def __str__(self):
        return self.product_name

class Order(models.Model):
    customer_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

