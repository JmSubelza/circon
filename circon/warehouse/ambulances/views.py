from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from circon.warehouse.ambulances.models import Ambulances
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import Create


class ListAmbulances(PaginationMixin, ListView):
    template_name = 'warehouse/ambulances/list.html'
    model = Ambulances
    paginate_by = 10


class DetailAmbulances(DetailView):
    template_name = 'warehouse/ambulances/detail.html'
    model = Ambulances
    paginate_by = 1


class CreateAmbulances(CreateView):
    form_class = Create
    initial = {'key': 'value'}
    template_name = 'warehouse/ambulances/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            ambulances = form.cleaned_data['ambulances']
            active = form.cleaned_data['active']
            p = Ambulances()
            p.ambulances = ambulances
            p.active = active
            p.save()
            return HttpResponseRedirect('/List_Ambulances')

        return render(request, self.template_name, {'form': form})


class UpdateAmbulances(UpdateView):
    template_name = 'warehouse/ambulances/update.html'
    model = Ambulances
    fields = ['ambulances', 'active']

    def get_success_url(self):
        return reverse('detail_ambulances', kwargs={'pk': self.object.pk})


class DeleteAmbulances(DeleteView):
    template_name = 'warehouse/ambulances/delete.html'
    model = Ambulances
    success_url = reverse_lazy('list_ambulances')
