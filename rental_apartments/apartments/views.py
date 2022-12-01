from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from . models import Apartment, Guest, Reservation, User


def index(request):
    apartment_count = Apartment.objects.count()
    reservation_count = Reservation.objects.count()
    # guest_count = Guest.objects.count()
    user_count = User.objects.count()
    visit_count = request.session.get('visit_count', 1)
    request.session['visit_count'] = visit_count + 1

    context = {
        'apartment_count' : apartment_count,
        'reservation_count' : reservation_count,
        'user_count' : user_count,
        'visit_count' : visit_count,
        }
    
    return render (request, 'apartments/index.html', context=context)

