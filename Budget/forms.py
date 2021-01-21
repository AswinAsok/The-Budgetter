from django import forms
from Budget.models import Budget

class CreateForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name','amount']


        