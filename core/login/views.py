import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, RedirectView

import config.settings as setting
from config import settings
from core.login.form import ResetPasswordForm
from core.user.models import User


class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


class LogoutView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class LoginFormView2(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy(setting.LOGIN_REDIRECT_URL)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


class ResetPasswordView(FormView):
    form_class = ResetPasswordForm
    template_name = 'reset_password.html'
    success_url = reverse_lazy(setting.LOGIN_REDIRECT_URL)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def send_email_reset_pwd(self, user):
        data = {}
        try:
            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            mailServer.starttls()
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            # email_to = "german03prueba@gmail.com"
            email_to = user.email

            mensaje = MIMEMultipart("""Este es el mensaje
             de las narices""")
            mensaje['From'] = settings.EMAIL_HOST_USER
            mensaje['To'] = email_to
            mensaje['Subject'] = "Recuperar Contraseña"

            content = render_to_string('login/send_email.html', {
                'user': user,
                'link_resetpwd': '',
                'link_home': ''
            })
            mensaje.attach(MIMEText(content, 'html'))

            mailServer.sendmail(settings.EMAIL_HOST_USER, email_to, mensaje.as_string())
            print('Correo enviado Correctamente espero ver este print por amor a Dios!')
        except Exception as e:
            data['error'] = str(e)
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                user = form.get_user()
                data = self.send_email_reset_pwd(user)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Recuperar contraseña'
        return context
