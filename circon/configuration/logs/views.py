from django.views.generic import ListView
from django.views.generic import TemplateView
from pure_pagination.mixins import PaginationMixin
from circon.warehouse.products.models import Products


class ListLogs(PaginationMixin, TemplateView):
    template_name = 'configuration/logs/tables.html'
    paginate_by = 10


class LogsProducts(PaginationMixin, ListView):
    template_name = 'configuration/logs/list.html'
    queryset = Products.audit_log.all()
    paginate_by = 10
