from django.contrib import admin
from . models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {"fields": ("username","name","email", "mobile","profile", "password", "department","role")}),
            ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        )
    add_fieldsets = (
            (None, {
                "classes": ("wide",),
                "fields": (
                    "username", "email", "name","email", "mobile","profile", "password", "department","role", "is_staff",
                    "is_active", "groups", "user_permissions"
                )}
            ),
        )