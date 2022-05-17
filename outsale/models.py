from django.db import models

from brands.models import Brand


class Outsale(models.Model):
    """outsale details with name,amount"""
    date = models.DateField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.IntegerField()
    name = models.CharField(max_length=30, default="Customer")
    udate = models.DateField(auto_now=True)

    def __str__(self):
        return self.brand.name + str(self.qty)

    def dis(self):
        dis = (self.brand.bprice - self.price) * self.qty
        return dis
