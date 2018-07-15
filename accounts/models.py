from django.contrib.auth import models as user_models
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from dictionaries.models import Gender, Interest


class Profile(models.Model):
    user = models.OneToOneField(user_models.User, on_delete=models.CASCADE)
    fb_id = models.CharField(max_length=128, null=True, blank=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(16)], null=True)
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

    def __str__(self):

        return self.user.username


@receiver(post_save, sender=user_models.User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
