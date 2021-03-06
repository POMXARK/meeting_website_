from django.contrib.auth.models import User
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from pilkit.lib import Image
from django.db import models
from django.utils.html import mark_safe

User._meta.get_field('email')._unique = True


class Watermark(object):
    def process(self, img):
        width, height = img.size
        watermark = Image.open('watermark.png')
        w_width, w_height = img.size
        watermark = watermark.resize((int(w_width / 5), int(w_height / 5)), Image.ANTIALIAS)
        img.paste(watermark, (int(width / 1.3), int(height / 1.25)), watermark)
        return img


class Person(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    sympathy = models.ManyToManyField('Person', blank=True, symmetrical=False)
    latitude = models.FloatField(max_length=30)
    longitude = models.FloatField(max_length=30)

    avatar = ProcessedImageField(upload_to='avatars',
                                 processors=[ResizeToFill(400, 400), Watermark()],
                                 format='JPEG',
                                 options={'quality': 60}, blank=True)

    @property
    def thumbnail_preview(self):
        if self.avatar:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.avatar.url))
        return ""

    def __str__(self):
        return self.first_name + " " + self.last_name
