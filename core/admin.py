from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.forms import UserCreationForm, UserChangeForm
from core.models import User, Article, Author, Tag

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'gender')}),
        ('Contact info', {'fields': ('email', 'mobile_phone')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Login Info', {'fields': ('email', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Tag)