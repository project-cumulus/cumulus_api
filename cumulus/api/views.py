from django.shortcuts import render
from api.models import Subscription, SubscriptionTransactionHistory
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import SubscriptionSerializer, SubTransactionHistorySerializer, CreateSubscriptionSerializer


class SubscriptionListAV(APIView):
    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CreateSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SubscriptionDetailAV(APIView):
    def get(self, request, subscription_id):
        try:
            subscription = Subscription.objects.get(pk=subscription_id)
        except Subscription.DoesNotExist:
            return Response({'error': "Subscription not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)
        
    def patch(self, request, subscription_id):
        subscription = Subscription.objects.get(pk=subscription_id)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, subscription_id):
        subscription = Subscription.objects.get(pk=subscription_id)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class SubTransactionHistoryListAV(APIView):
    def get(self, request):
        transaction = SubscriptionTransactionHistory.objects.all()
        serializer = SubTransactionHistorySerializer(transaction, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SubTransactionHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    