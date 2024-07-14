from django.urls import path
from .views import *

urlpatterns = [
    path('login',custom_admin_login),
    path('user_list',user_list),
    path('admin_login',admin_login),
    path('add_new_user',add_users),
    path('add_user',add_user_temp),
    path('delete_user',delete_user),
    path('logout',logout)
]