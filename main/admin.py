from django.contrib import admin
from .models import User, Profile

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile', 'last_login', 'id')
    list_filter = ('username', 'mobile', 'last_login')
    exclude = ('first_name', 'last_name', 'last_login', 'date_joined', 'groups', 'user_permission')


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
