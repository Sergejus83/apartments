from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from . forms import ProfileUpdateForm, UserUpdateForm

User = get_user_model()

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        error = False

        if User.objects.filter(username=username).first() or not username:
            messages.error(request, _("Warning! Username not entered or already exists!"))
            error = True
        if User.objects.filter(email=email).first() or not email:
            messages.error(request, _("Warning! Email not entered or already exists!"))
            error = True
        else: 
            try:
                validate_email(email)
            except:
                messages.error(request, _("Warning! Invalid email!"))
                error = True
        if password != password_2 or not password or not password_2:
            messages.error(request, _("Warninig! Password not entered or not the same!"))
            error = True
        if not error:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, _('Successful! New user "') + f"{ username }" + _( '" created!'))
            return redirect('update_profile')
            
    return render(request, 'user_profile/register.html')


@login_required
def profile(request):
    return render(request, 'user_profile/profile.html')


@login_required
def update_profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Successful! User "') + f"{ request.user.username }" + _( '" updated!'))
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'user_profile/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })