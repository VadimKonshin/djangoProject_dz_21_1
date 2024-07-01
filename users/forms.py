from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixim
from users.models import User


class UserRegisterForm(StyleFormMixim, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'country', 'password1', 'password2')

