from django.shortcuts import render, redirect
from .models import FoodItem, Order
from .forms import OrderForm

# Create your views here.
def menu_list(request):
    food_items = FoodItem.objects.filter(is_available=True).order_by('created_at')
    return render(request, 'menu/menu_list.html', {'food_items': food_items})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                customer_name=form.cleaned_data['customer_name']
            )
            order.items.set(form.cleaned_data['items'])
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'menu/place_order.html', {'form': form})

def order_success(request):
    return render(request, 'menu/order_success.html')