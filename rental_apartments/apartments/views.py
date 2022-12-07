from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from . models import Apartment, Guest, Reservation, User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . forms import ReservationForm #, ReservationUpdateForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages



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


class UserReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'apartments/user_reservation_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter().order_by('-date_in')
        return queryset


class UserReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'apartments/user_reservation_create.html'
    success_url = reverse_lazy('user_reservations')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.status = 'r'
        messages.success(self.request, _('The apartment has been reserved!'))
        return super().form_valid(form)





