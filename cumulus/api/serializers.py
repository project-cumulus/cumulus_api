from rest_framework import serializers
from api.models import Subscription, SubscriptionTransactionHistory, ChaseTransaction
from decimal import *

class SubTransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionTransactionHistory
        fields = [
            "amount", "currency", "date_paid"
        ]
        
class CreateSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            "id",
            "subscription_name",
            "description",
            "active",
            "fixed",
            "discretionary", 
            "currency",
            "amount_per_frequency",
            "frequency",
            "frequency_detail",
            "payment_method",
            "category",
            "cancellation_url",
            "company_logo_url"
        ]
    def validate(self, data):
        if data['subscription_name'] == data['description']:
            raise serializers.ValidationError(
                "Title and Description should be different!"
            )
        
        return data

    def validate_subscription_name(self, value):
        
        if len(value) < 3:
            raise serializers.ValidationError("Name is too short")
    
        return value   
    
    def validate_payment_method(self, value):
        valid_payment_methods = {"amex", 'visa', 'mastercard', 'discover', 'bank account'}
        
        if value.lower() not in valid_payment_methods:
            raise serializers.ValidationError(
                "Payment method has not been added as a valid payment option"
            )
        
        return value
    
    def validate_currency(self, currency_code):
        valid_currencies = {"USD", "AUD", "EUR", "GBP", "MXN", "JPY", "HKD", "CAD", "NZD", "RMB"}
        
        if currency_code.upper() not in valid_currencies:
            raise serializers.ValidationError(
                "Currency code has not been added as a valid currency"
            )
    
        return currency_code
    
    def validate_amount_per_frequency(self, amount):
        if not (type(amount) == int or type(amount) == Decimal):
            raise serializers.ValidationError("Payment amount is not a number")
        
        if amount <= 0:
            raise serializers.ValidationError("Payment amount must be greater than $0.00")
        
        return amount
    
    
    def validate_frequency(self, frequency):
        valid_frequencies = {"weekly", "monthly", "quarterly", "yearly"}
        
        if frequency.lower() not in valid_frequencies:
            raise serializers.ValidationError("Frequency is not valid")
        
        return frequency
    
    def validate_category(self, category):
        valid_categories = {"Entertainment & Media", "Transportation", "Health & Wellbeing", "Finance & Insurance", "Technology", "Utilities"}
        
        if category not in valid_categories:
            raise serializers.ValidationError("Category does not currently exist")
    
        return category
    
class SubscriptionSerializer(serializers.ModelSerializer):
    transaction_history = SubTransactionHistorySerializer(many=True)
    
    class Meta:
        model = Subscription
        fields = [
            "id",
            "subscription_name",
            "description",
            "active",
            "fixed",
            "discretionary", 
            "currency",
            "amount_per_frequency",
            "frequency",
            "frequency_detail",
            "payment_method",
            "category",
            "cancellation_url",
            "company_logo_url",
            "transaction_history"
        ]

class ChaseTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChaseTransaction
        fields = "__all__"
        
    # def validate_discretionary(self, discretionary):
        
    #     if type(discretionary) != bool or type(discretionary) == str:
    #         raise serializers.ValidationError("Discretionary field must be a boolean")
        
    #     return discretionary
        

    # def validate_fixed(self, fixed):
    #     if type(fixed) != bool or type(fixed) == str:
    #         raise serializers.ValidationError("Fixed field must be a boolean")
    
    #     return fixed
        

    # def validate_active(self, active):
    #     if type(active) != bool or type(active) == str:
    #         raise serializers.ValidationError("Active field must be a boolean")
        
    #     return active

