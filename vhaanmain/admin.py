from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "kmsparivhaan super admin"
admin.site.register(user_custom)
admin.site.register(statelists)
admin.site.register(stateassigned)
admin.site.register(add_rajasthan)
admin.site.register(add_punjab)
admin.site.register(add_haryana)
admin.site.register(add_bihar)
admin.site.register(add_gujrat)
admin.site.register(add_gujrat_odc)
admin.site.register(add_himachal)
admin.site.register(add_jharkhand)
admin.site.register(add_karnataka)
admin.site.register(add_uttarpradesh)
admin.site.register(add_uttrakhand)
admin.site.register(add_madhyapradesh)
admin.site.register(add_maharashtra)
admin.site.register(add_tamilnadu)
admin.site.register(add_tripura)