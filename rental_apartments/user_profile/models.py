from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from PIL import Image

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name='profile',
        )
    photo = models.ImageField(_("photo"), upload_to='user_profile/photo', null=True, blank=True)
    photo_2 = models.ImageField(_("photo_2"), upload_to='user_profile/photo', null=True, blank=True)
    phot_3 = models.ImageField(_("photo_3"), upload_to='user_profile/photo', null=True, blank=True)
    photo_4 = models.ImageField(_("photo_4"), upload_to='user_profile/photo', null=True, blank=True)

    def __str__(self) -> str:
        return f'Profile: "{self.user}"'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            photo = Image.open(self.photo.path)
            if photo.width > 500 or photo.height > 500:
                output_size = (500, 500)
                photo.thumbnail(output_size)
                photo.save(self.photo.path)
                