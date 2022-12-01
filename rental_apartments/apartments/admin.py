from django.contrib import admin
from . import models


# class ReservationInline():
#     pass

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'apart_type', 'room', 'size', 'price', )
    # inlines = (ReservationInline,)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ( 'apartment', 'guest', 'status', 'date_in', 'date_out', 'total_price',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone',)

admin.site.register(models.Apartment, ApartmentAdmin)
admin.site.register(models.Guest, UserAdmin)
admin.site.register(models.Reservation, ReservationAdmin)
