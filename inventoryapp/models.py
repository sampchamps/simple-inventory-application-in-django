# Create Model for Simple Inventory
from django.db import models


# Create Class to define the model
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.category_name


class Item(models.Model):
    name_item = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_item
