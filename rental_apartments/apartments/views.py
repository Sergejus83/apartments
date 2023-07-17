from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from . models import Apartment, Reservation, User, Guest
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . forms import ReservationForm, ReservationUpdateForm, AparmentReviewForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.db.models import Q


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

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(city__icontains=search))
        apartment_id = self.request.GET.get('genre_id')
        if apartment_id:
            queryset = queryset.filter(city__id=apartment_id)
        return queryset


class ApartmentDetailView(FormMixin, DetailView):
    model = Apartment
    template_name = 'apartments/apartment_detail.html'
    form_class = AparmentReviewForm

    def get_success_url(self):
        return reverse('apartment', kwargs={'pk': self.get_object().id})

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            messages.error(self.request, "You posting too much. Posting limit 1 review/hour")
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.apartment = self.get_object()
        form.instance.guest = self.request.user
        form.save()
        messages.success(self.request, _("Your review was posted!"))
        return super().form_valid(form)

    def get_initial(self):
        return {
            'apartment': self.get_object(),
            # 'guest': self.request.user.guest,
        }


class UserReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'apartments/user_reservation_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(guest=self.request.user).order_by('-date_in')
        return queryset


class UserReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'apartments/user_reservation_create.html'
    success_url = reverse_lazy('user_reservations')

    def form_valid(self, form):
        form.instance.guest = self.request.user
        form.instance.status = 'r'
        messages.success(self.request, _('The apartment has been reserved!'))
        return super().form_valid(form)


class UserReservationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reservation
    form_class = ReservationUpdateForm
    template_name = 'apartments/user_reservation_update.html'
    success_url = reverse_lazy('user_reservations')

    def form_valid(self, form):
        form.instance.guest = self.request.user.guest
        form.instance.status = 'r'
        messages.success(self.request, _('Reservation was changed!'))
        return super().form_valid(form)

    def test_func(self):
        reservation = self.get_object()
        return self.request.user.guest == reservation.guest



class UserReservationDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Reservation
    template_name = 'apartments/user_reservation_delete.html'
    success_url = reverse_lazy('user_reservations')

    def test_func(self):
        reservation = self.get_object()
        return self.request.user.guest == reservation.guest

    def form_valid(self, form):
        reservation = self.get_object()
        if reservation.status == 'r':
            messages.success(self.request, _('Reservation CANCELLED!'))
        return super().form_valid(form)




