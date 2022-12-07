from django import forms
from . models import Reservation
from django.utils.translation import gettext_lazy as _


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('apartment', 'date_in', 'date_out')
        widgets = {'date_in': DateInput(), 'date_out': DateInput()}


# class ReservationUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ('apartment.name', 'date_in', 'date_out')
#         widgets = {'date_in': DateInput(), 'date_out': DateInput()}
