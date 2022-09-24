from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Category, GST, Discount, Product
from .serializers import CategorySerializer, GSTSerializer, DiscountSerializer, ProductSerializer
from rest_framework.filters import SearchFilter,OrderingFilter


# Generic CRUD View for Category model
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]



# Generic CRUD View for GST model
class GSTListCreateAPIView(generics.ListCreateAPIView):
    queryset = GST.objects.all()
    serializer_class = GSTSerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]

class GSTRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GST.objects.all()
    serializer_class = GSTSerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]



# Generic CRUD View for Discount model
class DiscountListCreateAPIView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]

class DiscountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]



# Generic CRUD View for Product model
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['p_name']
    pagination_class = PageNumberPagination

    #logic for stock quantity == reorder quantity
    # def get_queryset(self, *args, **kwargs):
    #     queryset = super(ProductListCreateAPIView, self).get_queryset(*args, **kwargs)
    #     # queryset = Product.objects.all()
    #     ps = self.request.GET.get('product_stock')                  #eg. 1000
    #     ro = self.request.GET.get('reorder_level')                  #eg.   5
    #     print("total quantity", ps)
    #     print("remaining quantity", ro)
    #     data = ps-2                              #CustomerOrder.objects.get('quantity'), data=1000-2
    #     if data == ro:
    #         print("Reorder level reached, please increase quantity of same product")
    #     return queryset

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]









import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import uuid
import os
# from django.utils import timezone
import datetime


from .models import ExcelFileUpload
class ExportImportExcel(APIView):
	def get(self, request):
		queryset = Product.objects.all()
		serializer = ProductSerializer(queryset, many=True)
		df = pd.DataFrame(serializer.data)
		print("pandas dataframe",df)
		# df.to_csv(f"{settings.BASE_DIR}/static/ExportProduct/{uuid.uuid4()}.csv", encoding='UTF-8', index=False)
		df.to_csv(f"{settings.BASE_DIR}/static/ExportProduct/{datetime.datetime.now()}.csv", encoding='UTF-8', index=False)
		return Response(status=status.HTTP_200_OK)
	def post(self, request):
		new_upload_file = request.FILES['files']
		print("file type is file : ", new_upload_file)
		exceled_upload_obj = ExcelFileUpload(excel_file_upload=new_upload_file)
		print("exceled_upload_obj file upload : ", exceled_upload_obj)
		df = pd.read_csv(f"{settings.BASE_DIR}/static/ImportProductPending/{exceled_upload_obj.excel_file_upload}", encoding='UTF-8')
		print("list od data", df.values.tolist())
		for i in df.values.tolist():
			print(i)
			print("Product id : ", i[0])
			print("Product name : ", i[1])
			print("Product Image : ", i[2])
			print("Product price : ", i[3])
			print("Product stock : ", i[4])
			print("Product unit : ", i[5])
			print("Product reorder level : ", i[6])
			print("Product category : ", i[7])
			print("Product vendor : ", i[8])
			print("Product discount : ", i[9])
			print("Product gst : ", i[10])
			Product.objects.create(
									p_id = i[0],
									p_name = i[1],
									category = i[2],
									p_img = i[3],
									p_price = i[4],
									vendor = i[5],
									product_stock = i[6],
									unit = i[7],
									reorder_level = i[8],
									discount = i[9],
									gst = i[10],
									)
			print(i)
		return Response(status=status.HTTP_200_OK)





























