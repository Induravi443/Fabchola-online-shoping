from atexit import register
from django.contrib import admin
from .models import *
from .models import Order
from .models import Favourite



 
 
"""
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'image', 'description')
admin.site.register(Catagory,CategoryAdmin)
"""
 
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite) 

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at')
    readonly_fields = ('delivery_instructions',)