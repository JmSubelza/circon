from django.views.generic import ListView
from circon.warehouse.products.models import Products
from pure_pagination.mixins import PaginationMixin


class Inventory(PaginationMixin, ListView):
    template_name = 'warehouse/inventory/list.html'
    model = Products
    paginate_by = 10
