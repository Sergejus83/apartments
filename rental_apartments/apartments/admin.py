from django.contrib import admin
from . import models


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'apart_type', 'room', 'size', 'price', )
    list_filter  = ('name', 'city',)
    search_fields = ('apart_type', 'city',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ( 'apartment', 'guest', 'status', 'date_in', 'date_out', 'total_price',)
    list_filter = ('status', 'guest', 'date_reserved', 'date_in', 'date_out', )
    search_fields = ('apartment__name', 'apartment__city')


class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone',)
    list_filter = ('user', )
    search_fields = ('user__first_name', 'user__last_name', 'user__email', )


admin.site.register(models.Apartment, ApartmentAdmin)
admin.site.register(models.Guest, GuestAdmin)
admin.site.register(models.Reservation, ReservationAdmin)
