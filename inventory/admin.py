from django.contrib import admin
from inventory.models import Item, Category
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'owner']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']