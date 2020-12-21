from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    publish_date = models.DateField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True) 

class Costumer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItems (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)