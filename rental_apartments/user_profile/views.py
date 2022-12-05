from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required


User = get_user_model()

@csrf_protect
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        error = False

        if not User.objects.filter(username=username).first or username:
            messages.error(request, _("Warning! Username not entered or already exists!"))
            error = True
        if not User.objects.filter(email=email).first() or email:
            messages.error(request, _("Warning! Email not entered or already exists!"))
            error = True
        else: 
            try:
                validate_email(email)
            except:
                messages.error(request, _("Warning! Invalid email!"))
        if password != password_2 or not password or not password_2:
            messages.error(request, _("Warninig! Password not entered or not the same!"))
            error = True

        if not error:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "OK")
            return redirect('login')
            # _('Successful! New user ') + f"{ username }" + _( 'created!')
        
    return render(request, 'user_profile/register.html')


@login_required
def profile(request):
    return render(request, 'user_profile/profile.html')


