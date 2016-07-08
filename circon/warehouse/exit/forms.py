from circon.sales.sale.models import Sale
from circon.sales.sale.models import SaleDetail
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django import forms


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'


class SaleDetailForm(forms.ModelForm):

    quan_request = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    # products = forms.ChoiceField(widget=forms.RadioSelect(attrs={'readonly': 'readonly'}), initial='1')

    class Meta:
        model = SaleDetail
        fields = '__all__'



SaleFormSet = inlineformset_factory(Sale, SaleDetail, form=SaleDetailForm,
                                    extra=1)
