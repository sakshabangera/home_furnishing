from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category,Product,Customer,Invoice
from .serializer import CustomerSerializer,CategorySerializer,ProductSerializer,InvoiceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


class CustomerRegister(APIView):
    def post(self,request):
        serializer=CustomerSerializer(data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
  
class CustomerLogin(APIView):
    def post(self,request):
        username= request.data.get('username')
        password= request.data.get('password')

        try:
            user= Customer.objects.get(username= username, password= password)
            return JsonResponse({'message': 'Login Successful'}, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

        
class CategoryGet(APIView):
    def get(self,request,*args,**kwargs):
        result=Category.objects.all()
        serializer=CategorySerializer(result,many=True,partial=True)
        return Response({'status':'success','category':serializer.data},status=status.HTTP_200_OK)
    
    
class CategoryPost(APIView):  
    permission_classes=[IsAuthenticated]  
    def post(self,request):
        serializer=CategorySerializer(data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class ProductGet(APIView):
    def get(self,request,*args,**kwargs):
        result=Product.objects.all()
        serializer=ProductSerializer(result,many=True,partial=True)
        return Response({'status':'success','products':serializer.data},status=status.HTTP_200_OK)


class ProductPost(APIView):  
    permission_classes=[IsAuthenticated]    
    def post(self,request):
        serializer=ProductSerializer(data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
class InvoiceView(APIView):      
    def post(self,request):
        serializer=InvoiceSerializer(data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,*args,**kwargs):
        result=Invoice.objects.all()
        serializer=InvoiceSerializer(result,many=True,partial=True)
        return Response({'status':'success','invoice':serializer.data},status=status.HTTP_200_OK)
    
class get_category_product(APIView):
    # permission_classes=[IsAuthenticated] 
    def get(self, request, *args, **kwargs):
        by_category= kwargs.get("category")
        
        try:
            id= Category.objects.get(type=by_category).id
            prod= Product.objects.filter(category_id=id)
            serializer= ProductSerializer(prod, many=True,partial=True)
            return Response({'message': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({'message': 'error', 'data': 'Invalid Category'}, status=status.HTTP_400_BAD_REQUEST)
    
class get_status_invoice(APIView):
    # permission_classes=[IsAuthenticated] 
    def get(self, request, *args, **kwargs):
        product_status = request.query_params.get('status')
        try:
            if product_status:
                invoice = Invoice.objects.filter(status=product_status)
            else:
                invoice = Invoice.objects.all()

            serializer = InvoiceSerializer(invoice, many=True)
            return Response({"message": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'error', 'data': 'Invalid Status'}, status=status.HTTP_400_BAD_REQUEST)