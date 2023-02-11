from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.erp.models import Sale
from core.reports.forms import ReportForm

from django.db.models.functions import Coalesce, Cast
from django.db.models import Sum, DecimalField


# Create your views here.

class ReportSaleView(TemplateView):
    template_name = 'sale/report.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Sale.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.cli.names,
                        s.date_joined.strftime('%Y-%m-%d'),
                        format(s.subtotal, '.2f'),
                        format(s.iva, '.2f'),
                        format(s.total, '.2f'),
                    ])

                subtotal = search.aggregate(r=Cast(Sum('subtotal', default=0 ), output_field=DecimalField())).get('r')
                iva = search.aggregate(r=Cast(Sum('iva', default= 0), output_field=DecimalField())).get('r')
                total = search.aggregate(r=Cast(Sum('total', default=0), output_field=DecimalField(','))).get('r')

                # subtotal = search.aggregate(r=Coalesce(Sum('subtotal'), 0)).get('r')
                # iva = search.aggregate(r=Coalesce(Sum('iva'), 0)).get('r')
                # total = search.aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                data.append([
                    '---',
                    '---',
                    '---',
                    format(subtotal),
                    format(iva),
                    format(total),
                ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de venta'
        context['entity'] = 'Reporte'
        context['list_url'] = reverse_lazy('sale_reports')
        context['form'] = ReportForm

        return context
