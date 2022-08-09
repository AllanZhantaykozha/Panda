from django.contrib import admin
from .models import Food, Category


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'photo', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'category', 'price')
    fields = ('title', 'content', 'photo', 'category', 'price', 'slug')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    fields = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
