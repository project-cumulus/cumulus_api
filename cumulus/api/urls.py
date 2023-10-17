from django.urls import path
from api.views import SubscriptionListAV, SubscriptionDetailAV, TransactionListAV, CreditTxListAV, SecurityListAV

urlpatterns = [
    path('subscriptions/', SubscriptionListAV.as_view(), name="subscription-list"),
    path('subscriptions/<int:subscription_id>', SubscriptionDetailAV.as_view(), name="subscription-detail"),
    path('transactions/', TransactionListAV.as_view(), name="transaction-list"),
    path('transactions/credit/', CreditTxListAV.as_view(), name="credit-transactions"),
    path('securities/', SecurityListAV.as_view(), name='investment-prices')
]
