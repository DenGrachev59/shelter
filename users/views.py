import random

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView

from users.forms import UserRegisterForm, UserPofileForm
# from users.forms import UserRegisterForm, UserPofileForm
from users.models import User
from users.services import send_new_password


# Create your views here.

class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зарегистрировались на нашей платформе',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]

        )

        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserPofileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):  # Редактирование текущего пользователя который вошел на сайт
        return self.request.user


@login_required
def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])

    request.user.set_password(new_password)
    request.user.save()
    send_new_password(request.user.email, new_password)

    return redirect(reverse('dogs:index'))
