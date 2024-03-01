from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    password=models.CharField(max_length=16)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Category(models.Model):
    type=models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    condition=models.CharField(max_length=100)
    noofdays=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    options=models.JSONField()
    rentaloptions=models.JSONField()

    def __str__(self):
        return self.name
    
class Invoice(models.Model):
    STATUS_CHOICES = [
        ('ORDERED', 'Ordered'),
        ('CANCELLED', 'Cancelled'),
        ('DELIVERED', 'Delivered'),
    ]
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    products = models.ManyToManyField(Product)
    status= models.CharField(max_length=50, choices=STATUS_CHOICES) 

    def __str__(self):
        return self.status

