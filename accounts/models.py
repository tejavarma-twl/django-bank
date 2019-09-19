from django.db import models

# Create your models here.
class Accounts(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=15, decimal_places=2)