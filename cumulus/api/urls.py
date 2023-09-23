from django.urls import path
from api.views import SubscriptionListAV, SubscriptionDetailAV

urlpatterns = [
    path('list/', SubscriptionListAV.as_view(), name="subscription-list"),
    path('<int:subscription_id>', SubscriptionDetailAV.as_view(), name="subscription-detail")
]
