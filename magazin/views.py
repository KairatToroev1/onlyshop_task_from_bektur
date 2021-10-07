from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


from magazin.models import Production, Category
from magazin.serializers import ProductionSerializer, CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    permission_classes = [IsAuthenticated,]

    def perfom_create(self,serializer):
        return serializer.save(owner=self.request.user)

    # def increase_raiting(self):

    @action(methods=['post', ], detail=True)
    def add_product_to_cart(self,request,*args,**kwargs):
        product = self.get_object()
        print(product.name)
        cart = request.user.cart
        cart.product.add(product)
        serializer = CartSerializer(instance=cart)
        return Response(serializer.data)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

