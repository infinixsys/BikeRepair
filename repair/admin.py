from django.contrib import admin

from repair.models import PlanName, AboutUs, Services, Notification, BookingDetails, Order, ClientReview, PlanUpdate

# Register your models here.

admin.site.register(PlanName)
admin.site.register(AboutUs)
admin.site.register(Services)
admin.site.register(Notification)
admin.site.register(BookingDetails)
admin.site.register(Order)
admin.site.register(ClientReview)
admin.site.register(PlanUpdate)
