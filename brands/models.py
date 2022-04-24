from django.db import models
# Create your models here.
class Brand(models.Model):
    CATEGORY = (
        ('L','Liquor'),
        ('B','Beer'),
        ('M','Misclenious'),
    )
    ncode = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=30)
    scode = models.CharField(max_length=10,unique=True, null=True, blank=True)
    type = models.CharField(max_length=100,choices=CATEGORY)
    price = models.IntegerField()
    qty = models.IntegerField()
    mrp = models.IntegerField()
    bprice = models.IntegerField()

    def __str__(self):
        return self.name

    def iprice(self):
        ip=int(self.price/self.qty)
        return ip
