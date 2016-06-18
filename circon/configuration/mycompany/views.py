from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import CreateForm
from .models import MyCompany


class ListMyCompany(PaginationMixin, ListView):
    template_name = 'configuration/mycompany/list.html'
    model = MyCompany
    paginate_by = 10


class DetailMyCompany(DetailView):
    template_name = 'configuration/mycompany/detail.html'
    model = MyCompany
    paginate_by = 1


class CreateMyCompany(CreateView):
    model = MyCompany
    form_class = CreateForm
    initial = {'key': 'value'}
    template_name = 'configuration/mycompany/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            rif = form.cleaned_data['rif']
            p = MyCompany()
            p.name = name
            p.email = email
            p.address = address
            p.phone = phone
            p.rif = rif
            p.save()
            return HttpResponseRedirect('/List_MyCompany')

        return render(request, self.template_name, {'form': form})


class UpdateMyCompany(UpdateView):
    template_name = 'configuration/mycompany/update.html'
    model = MyCompany
    fields = "__all__"

    def get_success_url(self):
        return reverse('detail_user', kwargs={'pk': self.object.pk})


class DeleteMyCompany(DeleteView):
    template_name = 'configuration/mycompany/delete.html'
    model = MyCompany
    success_url = reverse_lazy('list_mycompany')
