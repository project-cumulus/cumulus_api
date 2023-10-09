from django.urls import path
from api.views import SubscriptionListAV, SubscriptionDetailAV, SubTransactionHistoryListAV, ChaseTransactionListAV

urlpatterns = [
    path('list/', SubscriptionListAV.as_view(), name="subscription-list"),
    path('<int:subscription_id>', SubscriptionDetailAV.as_view(), name="subscription-detail"),
    path('transactions/', SubTransactionHistoryListAV.as_view(), name="transaction-list"),
    path('chase_transactions/', ChaseTransactionListAV.as_view(), name="chase-transactions")
    
]
