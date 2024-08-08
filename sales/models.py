from django.db import models
from inventory.models import Product

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    company = models.CharField(max_length=100, blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name
    
class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING','Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED','Cancelled'),
    ]
    
    order_number = models.IntegerField(unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=60, choices=ORDER_STATUS_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return self.order_number
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
    
    