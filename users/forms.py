from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)      #previous
        fields = ('username', 'first_name', 'last_name', 'email', 'college',)          #new

    def clean(self):     # adding to check case-insensitive unique username
        cleaned_data = super(CustomUserCreationForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if ('@') in username:
            self.add_error('username', '@ symbol is not allowed in username.')
        if username and CustomUser.objects.filter(username__iexact=username).exists():
            self.add_error('username', 'A user with that username already exists.')
        if email and CustomUser.objects.filter(email__iexact=email).exists():
            self.add_error('email', "A user with that email already exists.")
        if ('gmail') in email.lower():
            if email.count('@') > 1:
                index_of_separator = email.rfind('@')
                email_local, email_domain = email[:index_of_separator], email[index_of_separator + 1:]
            else: # if email.count == 1:
                email_local, email_domain = email.split('@')
            if email and CustomUser.objects.filter(email__iexact=email_local+'@googlemail.com').exists():
                self.add_error('email', "A user is already registered using GoogleMail.com")
        if ('googlemail') in email.lower():
            if email.count('@') > 1:
                index_of_separator = email.rfind('@')
                email_local, email_domain = email[:index_of_separator], email[index_of_separator + 1:]
            else: # if email.count == 1:
                email_local, email_domain = email.split('@')
            if email and CustomUser.objects.filter(email__iexact=email_local+'@gmail.com').exists():
                self.add_error('email', "A user is already registered using Gmail.com")
        return cleaned_data

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
        # fields = ('avatar', 'bio', 'college', 'university', 'occupation', 'honours', 'degree', 'age')
        fields = ('bio', 'college', 'university', 'occupation', 'honours', 'degree', 'age')
