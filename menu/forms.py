from django import forms
from .models import FoodItem

class OrderForm(forms.Form):
    customer_name = forms.CharField(label='Your Name', max_length=100)
    customer_email = forms.EmailField()
    Date = forms.DateTimeField()
    items = forms.ModelMultipleChoiceField(
        queryset=FoodItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select Food Items'
    )