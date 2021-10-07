from rest_framework import serializers
from magazin.models import Production, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = ['category','description' , 'name','quantity','available' ,'created_at', ' updated ','number_of_products_in_stock', 'raiting', 'price']
