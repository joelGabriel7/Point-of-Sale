from django.urls import path

from core.login.views import *

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset/password/', ResetPasswordView.as_view(), name='recuperar_contraseña'),
    # path('logout/', LogoutRedirectView.as_view(), name='logout')
]
