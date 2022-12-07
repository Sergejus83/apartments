from django import forms
from . models import Reservation
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        date_in = cleaned_data.get("date_in")
        date_out = cleaned_data.get("date_out")
        apartment = cleaned_data.get("apartment")
        reservations = Reservation.objects.filter(
            apartment=apartment,
            date_in__gte=date_in,
            date_in__lt=date_out,
            date_out__gt=date_in,
            date_out__lte=date_out
        )
        if reservations.count() > 0:
            raise ValidationError(_("Sorry! This apartment already booked on these dates!"))


    class Meta:
        model = Reservation
        fields = ('apartment', 'date_in', 'date_out')
        widgets = {'date_in': DateInput(), 'date_out': DateInput()}


class ReservationUpdateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('apartment', 'date_in', 'date_out')
        widgets = {'apartment': forms.HiddenInput(), 'date_in': DateInput(), 'date_out': DateInput()}
