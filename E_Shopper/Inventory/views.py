from rest_framework import generics, viewsets
from .models import Category, GST, Discount, Product
from .serializers import CategorySerializer, GSTSerializer, DiscountSerializer, ProductSerializer
from rest_framework.views import APIView
from .models import Product
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse



# Generic CRUD View for Category model
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = []
    # authentication_classes = []

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = []
    # authentication_classes = []



# Generic CRUD View for GST model
class GSTListCreateAPIView(generics.ListCreateAPIView):
    queryset = GST.objects.all()
    serializer_class = GSTSerializer
    # permission_classes = []
    # authentication_classes = []

class GSTRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GST.objects.all()
    serializer_class = GSTSerializer
    # permission_classes = []
    # authentication_classes = []



# Generic CRUD View for Discount model
class DiscountListCreateAPIView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    # permission_classes = []
    # authentication_classes = []

class DiscountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    # permission_classes = []
    # authentication_classes = []



# Generic CRUD View for Product model
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = []
    # authentication_classes = []

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = []
    # authentication_classes = []

class ExportImportExcel(APIView):

    def get(self,request):
        product_obj = Product.objects.all()
        serializer = ProductSerializer(product_obj,many=True)
        df = pd.dataframe(serializer.data)
        print(df)

        return Response({'status:200'})


































