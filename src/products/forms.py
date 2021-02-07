from django import forms


from .models import Product


class RawProductForm(forms.Form):
	title		= forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
	description	= forms.CharField(
									label='',	 
									widget=forms.Textarea(attrs={
										"rows":10,
										"cols":120,
										"placeholder":"Please, add a description"}
										)
									)
	price		= forms.DecimalField(initial=0.0, )