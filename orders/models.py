from django.db import models

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    products_list = models.TextField()
    total_amount = models.IntegerField()
    estimated_delivery_date = models.DateTimeField(auto_now=True)
