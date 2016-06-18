from .models import Sale
from .models import SaleDetail
from django.forms import ModelForm
from django.forms.models import inlineformset_factory


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'

SaleFormSet = inlineformset_factory(Sale, SaleDetail,
                                    fields='__all__', extra=1)
