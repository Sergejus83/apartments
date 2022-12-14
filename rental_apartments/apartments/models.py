from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import datetime

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
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    photo = models.ImageField(_("photo"), upload_to='photo', blank=True, null=True)
    photo_2 = models.ImageField(_("photo"), upload_to='photo', blank=True, null=True)
    photo_3 = models.ImageField(_("photo"), upload_to='photo', blank=True, null=True)
    photo_4 = models.ImageField(_("photo"), upload_to='photo', blank=True, null=True)
    photo_5 = models.ImageField(_("photo"), upload_to='photo', blank=True, null=True)
    photo_6 = models.ImageField(_("photo"), upload_to='photo', blank=True, null=True)

    def __str__(self) -> str:
        # return f'Apartment: {self.name}, type: {self.apart_type}, {self.city}. Size {self.size}m2, price: {self.price} Eur'
        return self.name

class Guest(models.Model):
    user = models.OneToOneField(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='guest',
        )
    phone = models.CharField(_("phone number"), max_length=20)

    def __str__(self) -> str:
        return f'{self.user} {self.phone}'
    

class Reservation(models.Model):
    guest = models.ForeignKey(
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
    total_nights = models.IntegerField(_("total nights"), default=0)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(_("total price"), max_digits=10, decimal_places=2, default=0)
    RESERVATION_STATUS = (
        ('r', _('reserved')),
        ('c', _('canceled')),
        ('a', _('available')),
        ('p', _('past')),
        ('n', _('no info'))
    )
    status = models.CharField(_("status"), max_length=1, choices=RESERVATION_STATUS, default='n')

    def get_total_nights(self):
        return self.date_out - self.date_in

    @property
    def total_price(self):
        return self.total_nights * self.price

    def save(self, *args, **kwargs):
        self.total_nights = self.get_total_nights().days
        super().save(*args, **kwargs)

    @property
    def date_in_is_overdue(self):
        if self.date_in and self.date_in < datetime.date(datetime.now()):
            return True
        return False

    class Meta:
        ordering = ['date_in']

    @property
    def date_out_is_overdue(self):
        if self.date_out and self.date_out < datetime.date(datetime.now()):
            return True
        return False

    def __str__(self) -> str:
        return f'ID: {self.id}  ||  from {self.date_in} to {self.date_out}  ||  total: {self.total_nights}d./ {self.total_price} Eur'
    

class ApartmentReview(models.Model):
    apartment = models.ForeignKey(
        Apartment, 
        verbose_name=_("Apartment"), 
        on_delete=models.CASCADE,
        related_name='reviews'
        )
    guest = models.ForeignKey(
        User, 
        verbose_name=_("Guest"), 
        on_delete=models.CASCADE,
        related_name='apartment_reviews'
        )
    comment = models.TextField(_("Comment"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    photo_1 = models.ImageField(_("photo_1"), upload_to='photo', blank=True, null=True)
    photo_2 = models.ImageField(_("photo_2"), upload_to='photo', blank=True, null=True)
    photo_3 = models.ImageField(_("photo_3"), upload_to='photo', blank=True, null=True)



    def __str__(self):
        return f"{self.guest} on {self.apartment} at {self.created_at}"

    class Meta:
        ordering = ('-created_at', )
