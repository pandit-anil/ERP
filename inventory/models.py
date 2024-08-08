from django.db import models
from account.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    SKU = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'
    
    def __str__(self):
        return self.name
    
    