from django.urls import path
from api.views import SubscriptionListAV, SubscriptionDetailAV, TransactionListAV

urlpatterns = [
    path('subscriptions/', SubscriptionListAV.as_view(), name="subscription-list"),
    path('subscriptions/<int:subscription_id>', SubscriptionDetailAV.as_view(), name="subscription-detail"),
    path('transactions/', TransactionListAV.as_view(), name="transaction-list")
]
