from django.db import models

# Create your models here.
class GeneralSettings(models.Model):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
    )

    parameter = models.TextField(
        default='',
        max_length=255,
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