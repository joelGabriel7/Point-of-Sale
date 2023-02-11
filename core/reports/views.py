from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from core.reports.forms import ReportForm


# Create your views here.

class ReportSaleView(TemplateView):
    template_name = 'sale/report.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = 'Reporte de venta'
        context['entity'] = 'Reporte'
        context['list_url'] = reverse_lazy('sale_reports')
        context['form'] = ReportForm

        return context
