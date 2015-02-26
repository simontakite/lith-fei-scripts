from django import forms

class AddForm(forms.Form):
   title = forms.CharField(max_length=100)
   year = forms.CharField(max_length=4)
   director = forms.CharField(max_length=100)

