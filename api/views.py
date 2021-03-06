from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Author, Book, Costumer, Order, OrderItems
from .serializers import AuthorSerializer, BookSerializer, CostumerSerializer, OrderSerializer, OrderItemsSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookList (APIView):
    def get(self, request, format=None):
        try:
            author = request.query_params["author"]
            books = Book.objects.filter(author=author)
        except:
            books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail (APIView):
    def get_objects(self,pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk, format=None):
        try:
            book = self.get_objects(pk)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk, format=None):
        try:
            book = self.get_objects(pk)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            book = self.get_objects(pk)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CostumerViewSet(viewsets.ModelViewSet):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer

class OrderList(APIView):
    def get (self, request, format=None):
        try:
            parametro = request.query_params["costumer"]
            orders = Order.objects.filter(costumer=parametro)
        except:
            orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderDetail(APIView):
    def get(self, request, pk, format=None):
        order = get_object_or_404(Order.objects.all(),pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        order = get_object_or_404(Order.objects.all(),pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = get_object_or_404(Order.objects.all(),pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

