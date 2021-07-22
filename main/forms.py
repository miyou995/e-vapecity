from django import forms 



class MajorForm(forms.Form):
    major = forms.BooleanField(required=True)