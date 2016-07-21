from django.views.generic import ListView
from django.views.generic import TemplateView
from pure_pagination.mixins import PaginationMixin
from circon.warehouse.products.models import Products
from circon.warehouse.category.models import Category
from circon.warehouse.ambulances.models import Ambulances
from circon.warehouse.units_measures.models import UnitsMeasures
from circon.sales.sale.models import Sale
from circon.sales.sale.models import SaleDetail
from circon.purchases.purchase.models import Purchase
from circon.purchases.purchase.models import PurchaseDetail


class ListLogs(PaginationMixin, TemplateView):
    template_name = 'configuration/logs/listlogs.html'
    paginate_by = 10


class LogsProducts(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsproducts.html'
    queryset = Products.audit_log.all()
    paginate_by = 10


class LogsEntry(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsentry.html'
    queryset = Purchase.audit_log.all()
    paginate_by = 10


class LogsEntryDetail(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsentrydetail.html'
    queryset = PurchaseDetail.audit_log.all()
    paginate_by = 10


class LogsExit(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsexit.html'
    queryset = Sale.audit_log.all()
    paginate_by = 10


class LogsExitDetail(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsexitdetail.html'
    queryset = SaleDetail.audit_log.all()
    paginate_by = 10


class LogsRequest(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsrequest.html'
    queryset = SaleDetail.audit_log.all()
    paginate_by = 10


class LogsAmbulances(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsambulances.html'
    queryset = Ambulances.audit_log.all()
    paginate_by = 10


class LogsUnitsMeasures(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsunitsmeasures.html'
    queryset = UnitsMeasures.audit_log.all()
    paginate_by = 10


class LogsCategory(PaginationMixin, ListView):
    template_name = 'configuration/logs/logscategory.html'
    queryset = Category.audit_log.all()
    paginate_by = 10
