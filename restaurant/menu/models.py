from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('starters', 'Starters'), ('noodles', 'Noodles'), ('rice', 'Rice'),
        ('main', 'Main Course'), ('breads', 'Breads'),
        ('desserts', 'Desserts'), ('drinks', 'Drinks'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='main')
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='dishes/')
    is_veg = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name