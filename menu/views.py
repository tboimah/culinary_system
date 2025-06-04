from django.shortcuts import render, redirect
from .models import FoodItem, Order, OrderItem
from .forms import OrderForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def menu_list(request):
    food_items = FoodItem.objects.filter(is_available=True).order_by('created_at')
    return render(request, 'menu/menu_list.html', {'food_items': food_items})

def place_order(request):
    if request.method == 'POST':
        item_ids = request.POST.getlist('items')  
        order = Order.objects.create(customer_name=request.POST['customer_name'])

        for item_id in item_ids:
            order.items.add(item_id)

        return redirect('order-success')
    else:
        menu = FoodItem.objects.all()
        return render(request, 'menu/place_order.html', {'menu': menu})

def order_success(request):
    return render(request, 'menu/order_success.html') 


@login_required
def staff_order_dashboard(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')
        new_status = request.POST.get('status')
        order = order.objects.get(id=order_id)
        order.status = new_status
        order.save()
        return redirect('staff_order_dashboard')

    orders = Order.objects.all().order_by('-id')
    return render(request, 'menu/staff_dashboard.html', {'orders': orders})