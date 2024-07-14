from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('supadmin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('admin/',include("custom_admin.urls")),
    path('',include('vhaanmain.urls'))
]