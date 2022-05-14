from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from user_profile.models import Profile
from django.urls import reverse


def base_ctx() -> dict:
    return {
        "nav": {
            "Регистрация": {
                "link": "register"
            },
            "Войти в аккаунт": {
                "link": "login"
            },
            "Выйти из аккаунта": {
                "link": "logout"
            }
        }
    }

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {**super().get_context_data(**kwargs), **base_ctx(), 'title': 'Регистрация'}
        return context

    def form_valid(self, form):
        user = form.save()
        profile = Profile(user=user)
        profile.save()
        login(self.request, user)
        return redirect(f'/profile/{user.id}')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {**super().get_context_data(**kwargs), **base_ctx(), 'title': 'Вход'}
        return context

    def get_success_url(self):
        return reverse('profile', args=(self.request.user.id,))


def logout_view(request):
    logout(request)
    return redirect("register")