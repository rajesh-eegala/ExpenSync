from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Options(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    expense_title=models.CharField(max_length=100)
    expense_type=models.CharField(max_length=100)
    date=models.DateField(default=timezone.now)
    amount=models.IntegerField()
    
    