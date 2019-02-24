from django.contrib import admin
from ffarm.models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'token',)
