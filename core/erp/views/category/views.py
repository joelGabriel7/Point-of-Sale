from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from core.erp.forms import CategoryForms
from core.erp.models import Category


def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJson()
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['title'] = 'Listado de Categorías'
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForms
    template_name = 'category/create.html'
    success_url =reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Agregar Nueva Categoria'
        # print(reverse_lazy('category_list'))
        return context
