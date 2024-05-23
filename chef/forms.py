from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'