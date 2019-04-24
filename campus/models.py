from django.db import models
from django.utils.translation import ugettext as _

from core.models import DefaultModel


class Branch(DefaultModel):
    name = models.CharField(_('Name'), max_length=550)
    # TBD direccion
    # TBD contacto

    def __str__(self):
        return '{} {}'.format(self.code, self.name)

    class Meta:
        ordering = ['code']
        verbose_name = _('Branch')
        verbose_name_plural = _('Branches')


class Career(DefaultModel):
    name = models.CharField(_('Name'), max_length=550)
    plan = models.CharField(_('Plan'), max_length=20)
    description = models.CharField(_('Description'), max_length=5500)
    correlative = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)

    class Meta:
        ordering = ['code']
        verbose_name = _('Career')
        verbose_name_plural = _('Careers')


class Matter(DefaultModel):
    career = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(_('Name'), max_length=550)
    correlative = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)

    class Meta:
        ordering = ['code']
        verbose_name = _('Matter')
        verbose_name_plural = _('Matters')


class Course(DefaultModel):
    name = models.CharField(_('Name'), max_length=550)
    matter = models.ManyToManyField(Matter)
    max_students = models.IntegerField(
        _('Maximum Students'), blank=True, null=True
    )
    min_students = models.IntegerField(
        _('Minimum Students'), blank=True, null=True
    )

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)

    class Meta:
        ordering = ['code']
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class Classroom(DefaultModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=550)
    capacity = models.IntegerField(
        _('Maximum Capacity'), blank=True, null=True
    )

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)

    class Meta:
        ordering = ['code']
        verbose_name = _('Classroom')
        verbose_name_plural = _('Classroom')


