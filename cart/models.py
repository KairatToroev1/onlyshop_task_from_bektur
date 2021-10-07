from django.db import models
from magazin.models import Production, Category
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE,related_name='cart')
    product = models.ManyToManyField(Production, through='CartProduct', related_name='carts')

    def __str__(self):
        return f'Корзина пользователя: {self.owner.username}'

#создает авто корзину когда созадется user с usertype.personal_cabinet

@receiver(post_save,sender=User)
def create_cart(sender,instance,created,**kwargs):
    if created and instance.user_type == User.UserType.PERSONAL_CABINET:
        Cart.objects.create(owner=instance)

class CartProduct(models.Model):
    person = models.ForeignKey(Production, on_delete=models.CASCADE, related_name='cartproduction')
    amount = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='cartproduct')

    def __str__(self):
        return f'В корзине {self.person}'
