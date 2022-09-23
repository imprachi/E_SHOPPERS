from django.urls import path
from .views import VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('vendor/', VendorListCreateAPIView.as_view(), name='VendorListCreateAPIView_url'),
    path('vendor/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(),name='VendorRetrieveUpdateDestroyAPIView_url'),
]