from rest_framework import routers
from .views import AuthorViewSet, BookList, BookDetail, CostumerViewSet, OrderList, OrderDetail, OrderItemsViewSet
from django.urls import path, include

author_router = routers.SimpleRouter()
author_router.register('authors', AuthorViewSet)

costumer_router = routers.SimpleRouter()
costumer_router.register('costumers', CostumerViewSet)

orderitems_router = routers.SimpleRouter()
orderitems_router.register('orderitems', OrderItemsViewSet)

urlpatterns = [
    path('', include(author_router.urls)),
    path('', include(costumer_router.urls)),
    path('', include(orderitems_router.urls)),
    path('books/', BookList.as_view()),
    path('books/<int:pk>', BookDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>', OrderDetail.as_view()),
]