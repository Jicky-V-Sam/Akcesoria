from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category,Accessories_Product,Customer,Order

class Accessories_ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','category']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Accessories_Product,Accessories_ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order)
