from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.name


class Production(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                             null=True, related_name='magazin')
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    quantity = models.PositiveIntegerField(verbose_name='Колличество', null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')

    available = models.BooleanField(default=True, verbose_name='Есть в наличии?')
    # created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    number_of_products_in_stock = models.IntegerField()
    raiting = models.IntegerField(default=5)

    def __str__(self):
        return self.name



