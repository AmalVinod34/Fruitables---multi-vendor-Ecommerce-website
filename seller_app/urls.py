from django.urls import path
from seller_app import views

urlpatterns = [
    path('seller_home',views.seller_home,name="seller_home"),
    path('seller_contact',views.seller_contact,name="seller_contact"),
    path('seller_edit',views.seller_edit,name="edit"),
    path('seller_update/<int:u_id>,<int:s_id>',views.seller_update,name="update"),
    path('add_product',views.add_product,name="add_product"),
    path('view_product',views.view_product,name="view_product"),
    path('edit_product/<int:id>',views.edit_product,name="edit_product"),
    path('delete_product/<int:id>',views.delete_product,name="delete_product"),
    path('order_details_',views.order_details_,name="order_details_"),
    path('confirm_order/<int:id>',views.confirm_order,name="confirm_order"),
    path('ready_order/<int:id>',views.ready_order,name="ready_order"),
    path('delivered_order/<int:id>',views.delivered_order,name="delivered_order"),
    path('reject_order/<int:id>',views.reject_order,name="reject_order"),
    
]
