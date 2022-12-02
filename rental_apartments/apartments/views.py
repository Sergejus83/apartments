from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from . models import Apartment, Guest, Reservation, User
from django.views.generic import ListView, DetailView


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


class ApartmentListView(ListView):
    model = Apartment
    template_name = 'apartments/apartment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apartment_count'] = self.get_queryset().count()
        return context



class ApartmentDetailView(DetailView):
    model = Apartment
    template_name = 'apartments/apartment_detail.html'
