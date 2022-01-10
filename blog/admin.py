from django.contrib import admin
from .models import CustomUser, Category
# Register your models here.


@admin.register(CustomUser)
class CustomAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'gender', 'dob', 'is_staff','password')
    fieldsets = [(None, {'fields': ['firstname', 'lastname', 'email', 'gender', 'dob',
                                    'contact', 'is_staff', 'is_active']}), ]
    list_filter = ('gender', 'is_active')
    search_fields = ('firstname',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('Blog_categories',)
# admin.site.register(Category)
