from django.views.generic import UpdateView
from registration.backends.default.views import RegistrationView
from apps.security.forms import AdministratorRegisterForm, UserProfileForm
from apps.security.models import UserProfile


class AdministratorRegister(RegistrationView):
    form_class = AdministratorRegisterForm

class ProfileView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'security/profile.html'