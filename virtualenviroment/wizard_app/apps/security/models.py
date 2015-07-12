from django.contrib.auth.models import User
from django.db import models


class Appointment(models.Model):
    appointment = models.CharField(max_length=50)

    def __unicode__(self):
        return self.appointment


class Navegation(models.Model):
    nav = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nav


class Access(models.Model):
    appointment = models.ForeignKey(Appointment)
    navegation = models.ManyToManyField(Navegation)

    def __unicode__(self):
        return self.appointment.appointment


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    avatar = models.ImageField(upload_to='/profile/', blank=True)
    company = models.CharField(max_length=100)
    appointment = models.ForeignKey(Appointment, null=True, blank=True, default='')

    class Meta:
        verbose_name_plural = 'Profiles'

    def __unicode__(self):
        return self.user.username