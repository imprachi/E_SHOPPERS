from django.urls import path
from .views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView
from .views import GSTListCreateAPIView, GSTRetrieveUpdateDestroyAPIView
from .views import DiscountListCreateAPIView, DiscountRetrieveUpdateDestroyAPIView
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name='CategoryListCreateAPIView_url'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(),name='CategoryRetrieveUpdateDestroyAPIView_url'),

    path('gst/', GSTListCreateAPIView.as_view(), name='GSTListCreateAPIView_url'),
    path('gst/<int:pk>/', GSTRetrieveUpdateDestroyAPIView.as_view(),name='GSTRetrieveUpdateDestroyAPIView_url'),

    path('discount/', DiscountListCreateAPIView.as_view(), name='DiscountListCreateAPIView_url'),
    path('discount/<int:pk>/', DiscountRetrieveUpdateDestroyAPIView.as_view(),name='DiscountRetrieveUpdateDestroyAPIView_url'),

    #Inventory Url
    path('product/', ProductListCreateAPIView.as_view(), name='ProductListCreateAPIView_url'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),name='ProductRetrieveUpdateDestroyAPIView_url'),


    
]