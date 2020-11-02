from django import forms
from .models import Store, Candy, Buyer

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'store_name',
            'location',
            'description'
        ]

class CandyForm(forms.ModelForm):
    class Meta:
        model = Candy
        fields = [
            'name',
            'description',
            'ingredients',
            'price',
            'stock'
        ]

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = [
            'name',
            'location'
        ]