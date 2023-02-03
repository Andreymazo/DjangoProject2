from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from CustomUser.forms import CustomUserForm
from CustomUser.models import UserCustom


class CustomLoginView(LoginView):
    template_name = 'CustomUser/login.html'

class UserCustomProfileView(UpdateView):
    model = UserCustom
    template_name = 'CustomUser/profile.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('mailing_service:list')

    def get_object(self, queryset=None):
        return self.request.user