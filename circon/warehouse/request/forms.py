from django import forms
from circon.sales.sale.models import Sale
from circon.sales.sale.models import SaleDetail
from django.forms import ModelForm
from django.forms.models import inlineformset_factory


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'


class SaleDetailForm(ModelForm):
    class Meta:
        model = SaleDetail
        fields = '__all__'

    quan_request = forms.CharField(widget=forms.TextInput(
                                   attrs={'readonly': 'readonly'}))

SaleFormSet = inlineformset_factory(Sale, SaleDetail, form=SaleDetailForm,
                                    extra=2)


class SaleDetailForm(ModelForm):
    class Meta:
        model = SaleDetail
        fields = '__all__'


SaleFormSet = inlineformset_factory(Sale, SaleDetail, form=SaleDetailForm,
                                    extra=2)
