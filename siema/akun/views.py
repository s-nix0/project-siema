from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .forms import LoginForm


def create_temporary_user(username, password):
    # Create a temporary user with a unique username
    user = User.objects.create_user(username=username, password=password, first_name=username, is_staff=False, is_active=True)
    return user

def is_temporary_user(user):
    # Check if the user is temporary based on the date_joined field
    return (timezone.now() - user.date_joined) < timedelta(days=7)

def login_user(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Validate reCAPTCHA
            if not form.cleaned_data['captcha']:
                message = "reCAPTCHA verification failed. Please try again."
                messages.error(request, message)
                return redirect("login")

            # Continue with the existing username and password mechanism
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if is_temporary_user(user):
                    # User is temporary
                    login(request, user)
                    return redirect("dashboard")
                else:
                    # User is not temporary
                    login(request, user)
                    return redirect("dashboard")
            else:
                temporary_user = create_temporary_user(username, password)
                login(request, temporary_user)
                return redirect("dashboard")
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {'form': form})


# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect("dashboard")

#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect("dashboard")
#         else:
#             message = "Nama Pengguna atau Kata Sandi Salah, Coba Lagi"
#             messages.success(request, message)
#             return redirect("login")
#     else:
#         return render(request, "registration/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Anda telah keluar, silakan login kembali"))
    return redirect("login")


class AccountView(LoginRequiredMixin, ListView):
    template_name = "profil/index.html"
    model = User

    def get_queryset(self):
        # Return a queryset containing the current user
        return User.objects.filter(pk=self.request.user.pk)
