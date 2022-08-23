"""app URL Configuration

The `urlpatterns` list routes URLs to test. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function test
    1. Add an import:  from my_app import test
    2. Add a URL to urlpatterns:  path('', test.home, name='home')
Class-based test
    1. Add an import:  from other_app.test import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.homepage.views import  *
from core.login.views import  *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('erp/', include('core.erp.urls')),
    path('', IndexView.as_view(), name='main'),
    path('login/', include('core.login.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
