from django.db import models

# Create your models here.
class Loan(models.Model):
    STATUS =(
        ('Cleared','Cleared'),
        ('Not_Cleared','Not Cleared')
    )
    tdate = models.DateField()
    cdate = models.DateField(auto_now_add=True)
    udate = models.DateField(auto_now=True)
    name = models.CharField(max_length = 30)
    amount = models.IntegerField()
    roi = models.IntegerField()
    status = models.CharField(max_length=30,choices=STATUS)
    Purpose = models.TextField(blank=True,null=True)
    closedate = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name
