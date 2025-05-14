from django.contrib import admin
from .models import postadvert


@admin.register(postadvert)
class postadvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'city', 'category', 'description', 'image', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('title', 'description')
