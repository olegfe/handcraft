from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


#class CartAddProductForm(forms.Form):
   # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    #update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='Количество',max_value = 30 ,min_value = 1, widget=forms.NumberInput())
    #quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    