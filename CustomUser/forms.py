from django.contrib.auth.forms import UserChangeForm

from CustomUser.models import UserCustom


class CustomUserForm(UserChangeForm):
    class Meta:
        model = UserCustom
        fields = ('email', 'first_name', 'last_name','avatar')