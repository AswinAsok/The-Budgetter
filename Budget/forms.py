from django import forms
from Budget.models import Budget
from django.contrib.auth.models import User

class CreateForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = [ 'user','name','amount']

    def __init__(self, user, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(username=user)



        