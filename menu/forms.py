from django import forms
from .models import FoodItem

class OrderForm(forms.Form):
    customer_name = forms.CharField(label='Your Name', max_length=100)
    items = forms.ModelMultipleChoiceField(
        queryset=FoodItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select Food Items'
    )
