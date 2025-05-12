from django.db import models

# General Settings Model
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


# Ship Model
class Ship(models.Model):
    name = models.CharField(max_length=255)
    ship_type = models.CharField(max_length=255)
    gt = models.IntegerField()
    fuel_type = models.CharField(max_length=255)
    emission_level = models.DecimalField(max_digits=10, decimal_places=2)
    compliance_strategy = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.ship_type})"
