from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):# 「 UserCreationForm 」は「 ModelForm 」
    class Meta:
        model = User
        fields = ('username',)