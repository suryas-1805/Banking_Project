from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Account, Customer
from .serializers import AccountSerializer, CustomerSerializer

# Create your views here.
@api_view(['GET','POST'])
def accountlistview(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    account = Account.objects.all()
    serializer = AccountSerializer(account, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def accountdetailview(request,pk):
    try:
        account = Account.objects.get(account_id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AccountSerializer(account,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def customerlistview(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)

def index(request):
    account = Account.objects.all()
    customer = Customer.objects.all()
    context = {'account':account, 'customer':customer}
    return render(request,"index.html", context)
