from django.shortcuts import render
from api.models import Subscription, SubscriptionTransactionHistory, Transaction, Account, Security, SecPrice, Asset
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import SubscriptionSerializer, SubTransactionHistorySerializer, CreateSubscriptionSerializer, TransactionSerializer, AccountSerializer, SecuritySerializer, CreateSecuritySerializer, SecPriceSerializer, AssetSerializer


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
        serializer = CreateSubscriptionSerializer(subscription, data=request.data)
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

class TransactionListAV(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CreditTxListAV(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        data = serializer.data
        credits = {}
        
        for tx in data:
            if tx['details'] == "CREDIT":
                if tx['description'] in credits:
                    credits[tx['description']]['no_of_tx'] += 1
                    credits[tx['description']]['total_amount'] += float(tx['amount'])
                    
                else:
                    credits[tx['description']] = {
                        'no_of_tx': 1,
                        'total_amount': float(tx['amount'])
                    }
        
        output = []
        for payor in credits.keys():
            credits[payor]['total_amount']= round(credits[payor]['total_amount'], 2)
            output.append({
                'payor': payor,
                'no_of_tx': credits[payor]['no_of_tx'],
                'total_amount': credits[payor]['total_amount']
            })
            
        sorted_output = sorted(output, key=lambda x: x['total_amount'], reverse=True)
        return Response(sorted_output)
        
        
class AccountListAV(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def patch(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SecurityListAV(APIView):
    def get(self, request):
        securities = Security.objects.all()
        serializer = SecuritySerializer(securities, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CreateSecuritySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SecPriceListAV(APIView):
    def get(self, request):
        secPrices = SecPrice.objects.all()
        serializer = SecPriceSerializer(secPrices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SecPriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class AssetListAV(APIView):
    def get(self, request):
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def patch(self, request, asset_id):
        asset = Asset.objects.get(pk=asset_id)
        serializer = AssetSerializer(asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)