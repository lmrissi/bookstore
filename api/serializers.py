from rest_framework import serializers
from api.models import Author, Book, Costumer, Order, OrderItems

class AuthorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'birthday')

class BookSerializer (serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('author', 'title', 'pages', 'publish_date', 'price')

class CostumerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ('first_name', 'last_name', 'birthday', 'email')

class OrderSerializer (serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('costumer',)

class OrderItemsSerializer (serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ('order', 'book')