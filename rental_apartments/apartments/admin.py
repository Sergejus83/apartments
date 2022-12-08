from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'apart_type', 'room', 'size', 'price', )
    list_filter  = ('name', 'city',)
    search_fields = ('apart_type', 'city',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ( 'apartment', 'guest', 'status', 'date_in', 'date_out', 'total_price',)
    list_filter = ('status', 'guest', 'date_reserved', 'date_in', 'date_out', )
    search_fields = ('apartment__name', 'apartment__city',)


class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_first_name', 'get_last_name', 'get_email', 'phone',)
    list_filter = ('user', )
    search_fields = ('user__first_name', 'user__last_name', 'user__email', )


    @admin.display(description=_('Last name'), ordering='user__last_name')
    def get_last_name(self, obj):
        return obj.user.last_name

    @admin.display(description=_('First name'), ordering='user__first_name')
    def get_first_name(self, obj):
        return obj.user.first_name

    @admin.display(description=_('Email'))
    def get_email(self, obj):
        return obj.user.email


class ApartmentReviewAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'guest', 'created_at')
    


admin.site.register(models.Apartment, ApartmentAdmin)
admin.site.register(models.Guest, GuestAdmin)
admin.site.register(models.Reservation, ReservationAdmin)
admin.site.register(models.ApartmentReview, ApartmentReviewAdmin)
