from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)      #previous
        fields = ('username', 'first_name', 'last_name', 'email', 'college',)          #new

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields       #previous
        fields = ('username', 'first_name', 'last_name', 'email', 'college')   #new

class UserProfileForm(forms.ModelForm):
    """Form to update user profile."""

    # TODO: Define form fields here
    class Meta:
        model = CustomUser
        fields = ('avatar', 'bio', 'college', 'university', 'occupation', 'honours', 'degree', 'age')
