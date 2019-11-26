from django.contrib import admin

# Register your models here.
from .models import Manufacturer, Shoe, ShoeType, ShoeColor

admin.site.register(Manufacturer)
admin.site.register(Shoe)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)