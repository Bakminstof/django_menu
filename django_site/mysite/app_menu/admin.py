from django.contrib import admin

from app_menu.models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']

    def get_queryset(self, request):
        return Menu.objects.prefetch_related('items')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url_name', 'menu', 'parent']
    list_display_links = ['title']
    search_fields = ['name']

    def menu(self, obj: MenuItem):
        return obj.menu

    def parent(self, obj: MenuItem):
        return obj.parent
