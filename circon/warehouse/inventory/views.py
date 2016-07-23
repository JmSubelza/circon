from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectMixin
from circon.warehouse.products.models import Products
from circon.warehouse.category.models import Category
from pure_pagination.mixins import PaginationMixin
from django.http import HttpResponse


class Inventory(PaginationMixin, ListView):
    template_name = 'warehouse/inventory/list.html'
    model = Products
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(Inventory, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class SearchCategory(PaginationMixin, ListView):
    template_name = 'warehouse/inventory/list_category.html'
    paginate_by = 10

    def get_queryset(self):
        pk = self.kwargs['pk']
        products = Products.objects.filter(category_id=pk)
        return products

    def get_context_data(self, **kwargs):
        context = super(SearchCategory, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
