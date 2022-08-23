from django.urls import path

from core.erp.views.category.views import *
from core.erp.views.products.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.cliente.view import *
from core.erp.views.test.test import *

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    # Products
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # client
    path('client/', ClientView.as_view(), name='client'),
    # Home
    path('dashboard/', DashobardView.as_view(), name='dashboard'),
    # Test
    path('test/', TestView.as_view(), name='test'),

]
