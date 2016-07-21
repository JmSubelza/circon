from django.db import models
from audit_log.models.fields import LastUserField
from audit_log.models.managers import AuditLog


class Ambulances(models.Model):
    ambulances = models.CharField(max_length=10)
    active = models.BooleanField(default=True)

    audit_log = AuditLog()

    def __str__(self):
        return self.ambulances
