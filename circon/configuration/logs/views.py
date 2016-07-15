from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin
from circon.warehouse.products.models import Products


class ListLogs(PaginationMixin, ListView):
    template_name = 'configuration/logs/list.html'
    queryset = Products.audit_log.all()
    paginate_by = 10
