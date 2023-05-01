
from django import forms


class QA_Input(forms.ModelForm):

    body = forms.CharField(required=True)


    class Meta:


        exclude = ("user", )