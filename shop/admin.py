from django.contrib import admin
from .models import Product


@admin.register(Product)

class StarAdmin(admin.ModelAdmin):
    list_display = ['name',  'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', ]
    prepopulated_fields = {'slug': ('name',)}
    search_fields = (
        'name',
    )

