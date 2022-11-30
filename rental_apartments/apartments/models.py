from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# kuriam Modelius

User = get_user_model()


class Apartment(models.Model):
    name = models.CharField(_("name"), max_length=50)
    apart_type = models.CharField(_("type"), max_length=50)
    description = models.TextField(_("description"))
    city = models.CharField(_("city"), max_length=50)
    address = models.CharField(_("address"), max_length=50)
    size = models.DecimalField(_("size"), max_digits=5, decimal_places=2)
    room = models.IntegerField(_("room(s)"))
    bed = models.IntegerField(_("bed(s)"))
    sofa = models.IntegerField(_("sofa"), null=True)
    price = models.DecimalField(_(""), max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'Apartment: {self.name}, type: {self.apart_type}, {self.city}. Size {self.size}m2, price: {self.price} Eur'
    

class Guest(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='guest',
        )
    phone = models.CharField(_("phone number"), max_length=20)

    def __str__(self) -> str:
        return f'{self.user} {self.phone}'
    

class Reservation(models.Model):
    guest = models.OneToOneField(
        Guest, 
        verbose_name=_("guest"), 
        on_delete=models.CASCADE,
        related_name='reservations',
        )
    apartment = models.ForeignKey(
        Apartment, 
        verbose_name=_("apartment"), 
        on_delete=models.CASCADE,
        related_name='reservations',
        )
    date_reserved = models.DateField(_("date of reservation"), auto_now_add=True)
    date_in = models.DateField(_("date in"), null=True, blank=True)
    date_out = models.DateField(_("date out"), null=True, blank=True)
    # total_nights = models.IntegerField(_("total nights"))
    # price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    RESERVATION_STATUS = (
        ('r', _('reserved')),
        ('c', _('canceled')),
        ('a', _('available')),
        ('p', _('past')),
        ('n', _('no info'))
    )
    status = models.CharField(_("status"), max_length=1, choices=RESERVATION_STATUS, default='n')

    # @property
    # def total_nights(self):
    #     return self.date_out - self.date_in

    # @property
    # def total_price(self):
    #     return self.total_nights * self.price

    def __str__(self) -> str:
        return f'ID: {self.id}chek-in: {self.date_in}, check-out: {self.date_out}'
    



    
