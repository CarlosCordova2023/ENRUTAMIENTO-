from django.contrib import admin
from .models import Fabricante, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'f_vencimiento', 'fabricante')

admin.site.register(Fabricante)
admin.site.register(Producto, ProductoAdmin)
