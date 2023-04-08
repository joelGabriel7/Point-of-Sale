from config import wsgi
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
import smtplib
from config import settings
from email.mime.text import MIMEText

from core.user.models import User


def send_email():
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.ehlo()
        mailServer.starttls()
        print(mailServer.ehlo())
        # print(mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD))
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('conectado')

        # email_to = "german03prueba@gmail.com"
        email_to = "joelgerman671@gmail.com"

        mensaje = MIMEMultipart("""Este es el mensaje
        de las narices""")
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = "Tienes un correo probando"

        content = render_to_string('send_email.html', {'user': User.objects.get(pk=1)})
        mensaje.attach(MIMEText(content, 'html'))

        mailServer.sendmail(settings.EMAIL_HOST_USER, email_to, mensaje.as_string())
        print('Correo enviado Correctamente espero ver este print por amor a Dios!')
    except Exception as e:
        print(e)


send_email()
