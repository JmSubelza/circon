from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Permission
from django.forms.widgets import CheckboxSelectMultiple


class CreateForm(ModelForm):

    class Meta:
        model = User
        fields = ['groups', 'user_permissions']

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields["user_permissions"].widget = CheckboxSelectMultiple()
        self.fields["user_permissions"].queryset = Permission.objects.all()
        self.fields["groups"].widget = CheckboxSelectMultiple()
        self.fields["groups"].queryset = Group.objects.all()
