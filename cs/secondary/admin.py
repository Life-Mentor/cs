from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import User_Info, EmailVerifyRecord


admin.site.unregister(User)
"""
class UserProfileInline(admin.StackedInline):
    model = User

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]

admin.site.register(User, UserProfileAdmin)
"""

class UserProfileAdmin(admin.ModelAdmin):
    model = User_Info
admin.site.register(User_Info,UserProfileAdmin)

@admin.register(EmailVerifyRecord)
class Admin(admin.ModelAdmin):
    list_display = ('code',)



# Register your models here.
