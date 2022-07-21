from django.urls import path
from . import views
urlpatterns = [

    path('', views.MyfirstView, name='home'),
    path('dos', views.MySecondView),

]