from django.urls import path
from . import views
urlpatterns = [

    path('', views.MyfirstView),
    path('dos', views.MySecondView),

]