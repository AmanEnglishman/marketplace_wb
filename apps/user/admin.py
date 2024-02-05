from django.contrib import admin

from .models import MyUser, User


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
