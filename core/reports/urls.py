from django.urls import path

from core.reports.views import ReportSaleView

urlpatterns = [
    # category
    path('sale/',ReportSaleView.as_view(), name='sale_reports'),
]