from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views


def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'user/password_reset.html', {'form': form})

def password_reset_done(request):
    return render(request, 'user/password_reset_done.html')

def password_reset_confirm(request, uidb64, token):
    return auth_views.PasswordResetConfirmView.as_view()(request, uidb64=uidb64, token=token)

def password_reset_complete(request):
    return render(request, 'user/password_reset_complete.html')
