from django import forms 
from django.forms import NumberInput
# from django.core import validators
from .models import Order


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField( min_value=1, widget=NumberInput(attrs={'class': 'form-control text-center','value': 1, 'max':20 }))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CartAddProductQuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'addresse', 'email', 'birth_date' ,'phone', 'wilaya', 'commune', 'note']
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.fields['wilaya'] = forms.ModelChoiceField(queryset=Wilaya.objects.all()) 
    #     # self.fields['commune'] = forms.ModelChoiceField(queryset=Commune.objects.all()) 
    #     self.fields['commune'].queryset = Commune.objects.none()

    #     if 'wilaya' in self.data:
    #         try:
    #             wilaya_id = int(self.data.get('wilaya'))
    #             self.fields['commune'].queryset = Commune.objects.filter(Wilaya_id=wilaya_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass
    #     elif not 'wilaya' in self.data:
    #         self.fields['commune'].queryset = Commune.objects.none()