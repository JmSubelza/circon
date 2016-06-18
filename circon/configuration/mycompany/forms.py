from django import forms


class CreateForm(forms.Form):
    name = forms.CharField(label="Nombre", widget=forms. TextInput())
    email = forms.EmailField(label="Correo", required=False,
                             widget=forms.TextInput())
    address = forms.CharField(label="Address", required=False,
                              widget=forms.TextInput())
    phone = forms.CharField(label="Phone", required=False,
                            widget=forms.TextInput())
    rif = forms.CharField(label="Rif", required=False,
                          widget=forms.TextInput())
