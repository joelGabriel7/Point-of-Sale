from django.forms import *
from core.erp.models import *


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
            ),

        }
        exclude= ['user_creation', 'user_update']

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


    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Validacion error')
    #         # self.add_error('name', 'Error en guardar categoria')
    #     print(cleaned)
    #     return cleaned



class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'on'
        self.fields['name'].widget.attrs['autofocus'] = True


    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data