from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.ManyToManyField('FoodItem')
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    quantity = models.PositiveIntegerField(default=1)
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.items.name} x {self.quantity} - {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.food_item.name} (Order #{self.order.pk})"
