from django.db.models import Sum, DecimalField, FloatField
from django.db.models.functions import Cast
from django.views.generic import TemplateView
from datetime import *

from core.erp.models import Sale


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_graph_sales_year(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = Sale.objects.filter(date_joined__year=year, date_joined__month=m).aggregate(
                    r=Cast(Sum('total', default=0), output_field=FloatField())).get('r')
                data.append(total)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['graph_sales_year'] = self.get_graph_sales_year()
        return context
