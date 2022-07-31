from django.forms import *

from core.erp.models import Category


class CategoryForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Nombre'
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingresa un nombre',

                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingresa una descripcion ',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

    def save(self, commit=True):
        form = super()
        data = {}

        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors

        except Exception as e:
            data['error'] = str(e)
        return data