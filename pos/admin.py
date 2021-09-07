from django.contrib import admin
from .models import Product, Service

class ProductAdmin(admin.ModelAdmin):
    pass

class ServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)