from django.contrib import admin
from models import Brand, Category, Product
# Register your models here.

admin.site.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'description', 'update_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active','description',)
