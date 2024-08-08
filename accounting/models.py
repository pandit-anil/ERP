from django.db import models
from sales.models import Order

class Invoice(models.Model):
    INVOICE_STATUS_CHOICES =[
        ('UNPAID', 'Unpaid'),
        ('PAID', 'Paid'),
        ('OVERDUE', 'overdue'),
    ]
    
    invoice_number = models.IntegerField(unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    billing_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=INVOICE_STATUS_CHOICES)
    
    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        ordering = ['-billing_date']
        
    def __str__(self):
        return self.invoice_number
    
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('CREDIT_CARD', 'Credit Card'),
        ('ESEWA', 'Esewa'),
        ('KHALTI', 'Khalti'),
    ]
    
    invoice = models.ForeignKey(Invoice, on_delete= models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=70, choices=PAYMENT_METHOD_CHOICES)
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['-payment_date']
    
    def __str__(self):
        return f'{self.method} - {self.amount}'
    