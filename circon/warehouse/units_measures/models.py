from django.db import models


class UnitsMeasures(models.Model):
    units_measures = models.CharField(max_length=10)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.units_measures
