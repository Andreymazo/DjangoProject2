from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from CustomUser.apps import CustomuserConfig
from CustomUser.views import CustomLoginView, UserCustomProfileView

app_name = CustomuserConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile/', UserCustomProfileView.as_view(), name='profile'),
]

