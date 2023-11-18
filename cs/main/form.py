from django import forms

class SubmitBug(forms.Form):
    name = forms.CharField()
