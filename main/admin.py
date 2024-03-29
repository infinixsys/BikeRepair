from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from main.models import Profile, Role, RazorPay

User = get_user_model()


# register your models here.

class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']
    ordering = ['name']

    class Meta:
        model = Role


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'fname', 'phone', 'verified', 'otp',)
    list_ordering = ['id']
    list_filter = ('staff', 'active', 'role')
    fieldsets = (
        (None, {'fields': ('phone', 'otp')}),
        ('Personal info', {'fields': ('fname', 'lname', 'address', 'email')}),
        ('Permissions', {'fields': ('staff', 'active', 'super', 'role', 'verified', 'plan_user', 'booking_user', 'service_user', 'mechanic_user', 'customer_review_user', 'faq_user', 'support_user', 'account_user')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'otp')}
         ),
    )

    search_fields = ('phone', 'fname', 'role')
    ordering = ('phone', 'fname', 'id')
    filter_horizontal = ()

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
# Register onthersmodels
admin.site.register(Profile)


class RazorPayAdmin(admin.ModelAdmin):
    list_display = ('secret_key', 'public_key')


admin.site.register(RazorPay, RazorPayAdmin)
