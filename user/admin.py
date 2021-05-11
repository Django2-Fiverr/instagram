from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('username', 'email')
    list_display_links = ('username',)

    fieldsets = (
        ('personal_info',
                    {'fields': ('first_name', 'last_name', 'bio', 'avatar')}),
        ('account_information',
                    {'fields': ('username', 'password', 'email')}),
    )
