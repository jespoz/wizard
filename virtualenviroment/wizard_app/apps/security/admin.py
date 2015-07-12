from django.contrib import admin
from apps.security.models import Navegation, Access, Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Navegation)
class NavegacionAdmin(admin.ModelAdmin):
    pass

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    pass