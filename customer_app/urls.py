from django.urls import path
from customer_app import views

urlpatterns = [
    path('customer_home',views.customer_home,name="customer_home"),
    path('customer_shop',views.customer_shop,name="customer_shop"),
    path('customer_cart',views.customer_cart,name="customer_cart"),
    path('customer_checkout',views.customer_checkout,name="customer_checkout"),
    path('customer_contact',views.customer_contact,name="customer_contact"),
    path('edit',views.edit,name="edit"),
    path('update/<int:u_id>,<int:c_id>',views.update,name="update"),
    path('add_to_cart/<int:id>',views.add_to_cart,name="add_to_cart"),
    path('remove/<int:id>',views.remove_from_cart,name="remove_from_cart"),
    path('checkout',views.checkout,name="checkout"),
    path('order/<int:id>',views.order,name="order"),
    path('order_details',views.order_details,name="order_details"),
    
]
