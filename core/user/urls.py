from django.urls import path
from core.user.views import *


app_name = 'user'

urlpatterns = [
    # category
    path('list/', UserListView.as_view(), name='user_list'),
    # path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    # path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    # path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]