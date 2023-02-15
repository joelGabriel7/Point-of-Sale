from django.forms import *
from core.user.models import *


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'image'
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombre',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellido',

                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese su Email',

                }
            ),

            'username': TextInput(
                attrs={
                    'placeholder': 'Crea un Nombre de Usuario',

                }
            ),

            'password': PasswordInput(render_value=True,
                attrs={
                    'placeholder': 'Crea una Contraseña',

                }
            ),
        }
        exclude = [ 'groups', 'user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u=form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
