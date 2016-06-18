from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.category
