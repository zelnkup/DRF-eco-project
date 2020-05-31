from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyCustomUser


class MyCustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'code', 'points', 'is_active']


admin.site.register(MyCustomUser, MyCustomUserAdmin)

