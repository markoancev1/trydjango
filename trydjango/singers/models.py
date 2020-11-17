from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from datetime import datetime
# Create your models here.


def validate_age(value):
    if value == 0 and value > 150:
        raise ValidationError(
            _('%(value)s is not a correct age number'),
            params={'value': value},
        )


class Singer(models.Model):
    first_name = models.CharField(max_length=15, blank=False)
    last_name = models.CharField(max_length=15, blank=False)
    group = models.BooleanField(default=False)
    group_name = models.CharField(max_length=25, blank=True)
    from_macedonia = models.BooleanField(default=False)
    age = models.IntegerField(blank=False, validators=[validate_age])
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse("singers:singer-list", kwargs={"id": self.id})