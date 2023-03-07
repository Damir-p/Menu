from django.contrib import admin
from .models import MenuItem, Menu

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent')

class MenuAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
