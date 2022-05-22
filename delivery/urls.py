from django.urls import path
from delivery import views

urlpatterns = [
    path('orders/', views.order_list, name="order_list"),
    # path('shops/', views.shop, name="shop"),
    # path('menus/<int:shop>', views.menu, name="menu"),
]