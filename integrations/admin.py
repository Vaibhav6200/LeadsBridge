from django.contrib import admin
from .models import Integration


@admin.register(Integration)
class IntegrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'credentials', 'created_at')
    list_filter = ('user', 'created_at')
    ordering = ('-created_at',)

