from rest_framework.routers import SimpleRouter

from magazin.views import ProductViewSet, CategoryViewSet

router = SimpleRouter()

router.register('magazin', ProductViewSet)
router.register('magaz', CategoryViewSet)

urlpatterns = []

urlpatterns += router.urls