from django.contrib import admin
from .models import Order,OrderLines,Purchase,Product
# Register your models here.
admin.site.register(Product)
admin.site.register(Purchase)