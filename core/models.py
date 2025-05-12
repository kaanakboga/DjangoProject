from django.db import models

# Create your models here.
class GeneralSetting(models.Model):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )

    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    
    updated_date = models.DateTimeField(
        auto_now=True,
        blank=True,
    )

    create_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )