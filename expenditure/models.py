from django.db import models

# Create your models here.

class Exp(models.Model):
    #created date
    date = models.DateField()
    cdate = models.DateField(auto_now_add=True)
    #updated datea
    udate = models.DateField(auto_now=True)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    note = models.TextField(blank=True,null=True)

    def __str__(self):
        return (self.name+"  "+str(self.cdate))
