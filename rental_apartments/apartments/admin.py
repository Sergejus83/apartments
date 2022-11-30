from django.contrib import admin
from . import models


# class ReservationInline():
#     pass

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'apart_type', 'size', 'price')
    # inlines = (ReservationInline,)


admin.site.register(models.Apartment, ApartmentAdmin)
admin.site.register(models.Guest)
admin.site.register(models.Reservation)
