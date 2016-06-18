from django.db import models


class MyCompany(models.Model):
    name = models.CharField(max_length=200)
    rif = models.CharField(max_length=12)
    address = models.CharField(max_length=200, blank=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
