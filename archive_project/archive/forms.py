from django import forms

class SearchForm(forms.Form):
    q   = forms.CharField(label='Search string', max_length=100)

class DetailsForm(forms.Form):
    name         = forms.CharField(label='Your name', max_length=100)
    organisation = forms.CharField(label='Organisation', max_length=150, required=False)
    email        = forms.EmailField()


