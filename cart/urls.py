from rest_framework.routers import SimpleRouter
from cart.views import CartViewSet

router = SimpleRouter()

router.register('cart', CartViewSet)


urlpatterns = []

urlpatterns += router.urls