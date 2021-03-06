from django.db import models
from datetime import datetime    
from django.contrib.auth.models import User


# Create your models here.

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=50, blank=False)
    amount = models.FloatField(blank=False)
    date = models.DateField(default=datetime.now, blank=True)
    

    def __str__(self):
        return self.name

class MonthlyBudget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    max_amount = models.FloatField(blank=False)

    def __str__(self):
        return self.user.username