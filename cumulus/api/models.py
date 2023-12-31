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

class Account(models.Model):
    account_label = models.CharField(max_length=50)
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    joint = models.BooleanField(default=False)
    financial_institution = models.CharField(max_length=50)
    base_currency = models.CharField(max_length=3)
    date_opened = models.DateField()
    
    def __str__(self):
        return self.account_name
    
class Transaction(models.Model):
    currency = models.CharField(max_length=3)
    date = models.DateField()
    description = models.CharField(max_length=250)
    payee = models.CharField(max_length=50, blank=True)
    payor = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    isRecurring = models.BooleanField(default=False)
    account_id = models.ForeignKey(Account, related_name="account_relation", on_delete=models.SET_DEFAULT, default=None)
    # isShared = models.BooleanField(default=False)
    # isRefunded = models.BooleanField(default=False)
    # isExcluded = models.BooleanField(default=False)
    details = models.CharField(max_length=20, blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    # amount_gross = models.DecimalField(max_digits=20, decimal_places=2)
    # amount_net = models.DecimalField(max_digits=20, decimal_places=2)
    
    def __str__(self):
        return self.description

class Security(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    currency = models.CharField(max_length=3, blank=True)
    time_zone = models.CharField(max_length=50)
    last_refreshed = models.DateField()
    
    def __str__(self):
        return self.name

class SecPrice(models.Model):
    security = models.ForeignKey(Security, related_name="price_history", on_delete=models.CASCADE)
    date = models.DateField(default="2023-01-01")
    open = models.DecimalField(max_digits=20, decimal_places=4)
    high = models.DecimalField(max_digits=20, decimal_places=4)
    low = models.DecimalField(max_digits=20, decimal_places=4)
    close = models.DecimalField(max_digits=20, decimal_places=4)
    volume = models.IntegerField()
    
    def __str__(self):
        return self.close
    

class Asset(models.Model):
    currency = models.CharField(max_length=3)
    owner = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    offset_value = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    date = models.DateField()
    date_opened = models.DateField()
    date_closed = models.DateTimeField(blank=True, null=True)
    asset_type = models.CharField(max_length=50)
    asset_class = models.CharField(max_length=50)
    account_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.account_name