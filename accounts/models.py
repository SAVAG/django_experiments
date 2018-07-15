from django.contrib.auth import models as auth_models
from django.core.validators import MinValueValidator
from django.db import models

from dictionaries.models import Gender, Interest


class Profile(auth_models.User):
    GENDER_CHOICES = Gender.objects.gender_choices()
    INTEREST_CHOICES = Interest.objects.interest_choices()

    user = models.OneToOneField(auth_models.User, on_delete=models.CASCADE, parent_link=True)
    fb_id = models.CharField(max_length=128, null=True, blank=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(16)])
    gender = models.ForeignKey(
        Gender,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    interests = models.ManyToManyField(Interest)

    class Meta:
        db_table = 'profiles'
        managed = True


