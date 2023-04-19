from django.contrib import admin

from repair.models import PlanName, AboutUs, Services, Notification, BookingDetails, Order, ClientReview, PlanUpdate, \
    Support, FQA, Mechanic

# Register your models here.

admin.site.register(PlanName)
admin.site.register(AboutUs)
admin.site.register(Services)
admin.site.register(Notification)
admin.site.register(BookingDetails)
admin.site.register(Order)
admin.site.register(ClientReview)
admin.site.register(PlanUpdate)
admin.site.register(Support)
admin.site.register(FQA)
admin.site.register(Mechanic)