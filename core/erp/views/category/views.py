from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView

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

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):

      return super(CategoryListView, self).dispatch(request, *args,**kwargs)


    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['title'] = 'Listado de Categorías'
        return context
