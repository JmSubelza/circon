from circon.sales.sale.models import Sale
from circon.sales.sale.models import SaleDetail
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django import forms


class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = '__all__'


class SaleDetailForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SaleDetailForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['products'].widget.attrs['readonly'] = True

    def clean_products(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.products
        else:
            return self.cleaned_data['products']

    quan_request = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = SaleDetail
        fields = '__all__'


SaleFormSet = inlineformset_factory(Sale, SaleDetail, form=SaleDetailForm,
                                    extra=1)
