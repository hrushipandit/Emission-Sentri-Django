from django.db import models

class Emissions(models.Model):
    id = models.AutoField(primary_key=True)
    date_created = models.DateField(auto_now_add=True)
    accounting_period = models.CharField(max_length=255)
    scope_1 = models.IntegerField(null=True, blank=True)
    scope_2 = models.IntegerField(null=True, blank=True)
    scope_3 = models.IntegerField(null=True, blank=True)

