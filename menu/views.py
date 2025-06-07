from django.shortcuts import render, redirect
from .models import FoodItem, Order, OrderItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required


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


@login_required
def staff_dashboard(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')
        new_status = request.POST.get('status')
        order = order.objects.get(id=order_id)
        order.status = new_status
        order.save()
        return redirect('staff_dashboard')

  
    orders = Order.objects.all().order_by('-id')
    return render(request, 'menu/staff_dashboard.html', {'orders': orders,})


@login_required
def staff_order_dashboard(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'menu/staff_order_dashboard.html', {'orders': orders})
