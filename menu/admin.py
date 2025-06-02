from django.contrib import admin
from .models import FoodItem, Order

# Register your models here.
admin.site.register(Order)
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('is_available', 'created_at')