from django.views.generic import ListView
from circon.warehouse.products.models import Products
from pure_pagination.mixins import PaginationMixin


class Inventory(PaginationMixin, ListView):
    template_name = 'warehouse/inventory/list.html'
    model = Products
    paginate_by = 10


class Oils(ListView):
    queryset = Products.objects.filter(category='1')
    template_name = 'warehouse/inventory/oils.html'
    paginate_by = 10


class Rubbers(ListView):
    queryset = Products.objects.filter(category='2')
    template_name = 'warehouse/inventory/rubbers.html'
    paginate_by = 10


class Uniforms(ListView):
    queryset = Products.objects.filter(category='3')
    template_name = 'warehouse/inventory/uniforms.html'
    paginate_by = 10


class Stationery(ListView):
    queryset = Products.objects.filter(category='4')
    template_name = 'warehouse/inventory/stationery.html'
    paginate_by = 10


class Tools(ListView):
    queryset = Products.objects.filter(category='5')
    template_name = 'warehouse/inventory/tools.html'
    paginate_by = 10


class SuppliesMedical(ListView):
    queryset = Products.objects.filter(category='6')
    template_name = 'warehouse/inventory/suppliesmedical.html'
    paginate_by = 10
