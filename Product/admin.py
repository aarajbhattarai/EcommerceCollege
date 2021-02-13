from django.contrib import admin
from .models import Category, Product, SubCategory
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'status']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
