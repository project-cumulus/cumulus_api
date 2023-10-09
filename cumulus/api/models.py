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
    company_logo_url = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.subscription_name

class SubscriptionTransactionHistory(models.Model):
    subscription = models.ForeignKey(Subscription, related_name="transaction_history", on_delete=models.CASCADE)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    date_paid = models.DateField()
    
    class Meta:
        def __str__(self):
            return '%d: %s' % (self.amount, self.date_paid)


class ChaseTransaction(models.Model):
    debit = models.CharField(max_length=20)
    posting_date = models.DateField()
    description = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
