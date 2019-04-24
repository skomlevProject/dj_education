from django.db import models
from django.utils.translation import ugettext as _

from django.contrib.auth.models import AbstractUser

# from .managers import CustomUserManager


class User(AbstractUser):
    profile_image = models.URLField(
        max_length=200, null=True, blank=True, default=None)
    company = models.CharField(
        _('Company'), max_length=20, null=True, blank=True)
    office = models.CharField(
        _('Office'), max_length=20, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class DefaultModel(models.Model):
    code = models.CharField(_('Code'), max_length=20)
    active = models.BooleanField(_('Active'), default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['code']

    def __str__(self):
        return self.code
