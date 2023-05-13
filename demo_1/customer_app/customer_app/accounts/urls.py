from django.urls import path

from customer_app.accounts import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer', views.customer),
]