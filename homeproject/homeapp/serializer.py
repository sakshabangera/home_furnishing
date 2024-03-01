from rest_framework import serializers
from .models import Customer,Category,Product,Invoice
from django.contrib.auth import authenticate

class CustomerSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=100,required=True)
    last_name=serializers.CharField(max_length=100,required=True)
    username=serializers.CharField(max_length=100,required=True)
    email=serializers.CharField(max_length=100,required=True)
    phone=serializers.CharField(max_length=10,required=True)
    address=serializers.CharField(max_length=200,required=True)
    password=serializers.CharField(max_length=100,required=True)

    class Meta:
        model=Customer
        fields=('__all__')

class CategorySerializer(serializers.ModelSerializer):
    type=serializers.CharField(max_length=100,required=True)

    class Meta:
        model=Category
        fields=('__all__')

class ProductSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100,required=True)
    description=serializers.CharField(max_length=500,required=True)
    condition=serializers.CharField(max_length=100,required=True)
    noofdays=serializers.IntegerField(required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    options=serializers.JSONField()
    rentaloptions=serializers.JSONField()

    class Meta:
        model=Product
        fields=('__all__')


    
class InvoiceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    status= serializers.ChoiceField(choices=Invoice.STATUS_CHOICES)
    class Meta:
        model=Invoice
        fields=('__all__')