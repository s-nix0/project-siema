from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class AccountView(LoginRequiredMixin, ListView):
    template_name = "profil/index.html"
    model = User

    def get_queryset(self):
        # Return a queryset containing the current user
        return User.objects.filter(pk=self.request.user.pk)


def login_user(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            message = "Nama Pengguna atau Kata Sandi Salah, Coba Lagi"
            messages.success(request, message)
            return redirect("login")
    else:
        return render(request, "registration/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Anda telah keluar, silakan login kembali"))
    return redirect("login")
