from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('shop',views.shop,name="shop"),
    path('contact',views.contact,name="contact"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('login',views.us_login,name="us_login"),
    path('s_register',views.seller_register,name="seller_register"),
    path('register',views.user_register,name="user_register"),
    path('logout',views.us_logout,name="us_logout"),
    path('approve',views.approve,name="approve"),
    path('approve_seller/<int:id>',views.approve_seller,name="approve_seller"),
    path('view_customer',views.view_customer,name="view_customer"),
    path('view_seller',views.view_seller,name="view_seller"),
    path('seller_delete/<int:id>',views.reject_approval,name="reject_approval"),
    path('login_req',views.login_req,name="login_req"),
    
]
