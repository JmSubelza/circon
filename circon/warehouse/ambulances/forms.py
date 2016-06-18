from django import forms
from .models import Ambulances


class Create(forms.ModelForm):

    class Meta:
        model = Ambulances
        fields = ['ambulances', 'active']

    def clean_ambulances(self):
        ambulances = self.cleaned_data.get('ambulances', '')
        if len(ambulances) < 0:
            raise forms.ValidationError("Ingrese por lomenos 1 letra")
        return ambulances
