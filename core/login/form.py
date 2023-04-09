from django import forms

from core.user.models import User


class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su username',
        'autocomplete': 'off'
    }))

    def clean(self):
        cleaned = super().clean()
        if not User.objects.filter(username=cleaned['username']).exists():
            self._errors['error'] = self.errors.get('error', self.error_class([]))
            self._errors['error'].append('El usuario no exite')
            # raise forms.ValidationError('El usuario no existe')
        return cleaned


    def get_user(self):
        username = self.cleaned_data['username']
        return User.objects.get(username=username)
