from django import forms
from registration.forms import RegistrationForm
from apps.security.models import UserProfile


class AdministratorRegisterForm(RegistrationForm):

    def save(self, commit=True):
        user = super(AdministratorRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = True
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'