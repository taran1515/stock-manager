from django.db import models
from django.utils import timezone
# Create your models here.

class Purchase(models.Model):

    company = models.CharField(max_length=40)
    model_no = models.CharField(max_length=10)
    color = models.CharField(max_length=20,blank=True,null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=40, blank=True, null = True)
    date_of_purchase = models.DateField(default = None)

    def __str__(self):
        return "{} | {} | {}".format(self.company , self.model_no, self.date_of_purchase)



class Stock(models.Model):

    company = models.CharField(max_length=40,)
    model_no = models.CharField(max_length=10)
    color = models.CharField(max_length=20,blank=True,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return "{} | {}".format(self.company , self.model_no)

class Sale(models.Model):

    company = models.CharField(max_length=40)
    model_no = models.CharField(max_length=10)
    color = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    retailer = models.CharField(max_length=40,blank=True, null = True)
    date_of_sale = models.DateField(default = None)

    def __str__(self):
        return "{} | {} | {}".format(self.company , self.model_no, self.date_of_sale)




