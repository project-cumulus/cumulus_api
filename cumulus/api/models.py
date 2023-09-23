from django.db import models

class Subscription(models.Model):
    subscription_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=True)
    fixed = models.BooleanField(default=True)
    discretionary = models.BooleanField(default=True)
    currency = models.CharField(max_length=3)
    amount_per_frequency = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=20)
    frequency_detail = models.CharField(max_length=200, blank=True)
    payment_method = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    cancellation_url = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.subscription_name
    

