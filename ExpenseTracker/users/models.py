from django.db import models

# Create your models here.
class Options(models.Model):
    
    expense_title=models.CharField(max_length=100)
    expense_type=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    amount=models.IntegerField()
    