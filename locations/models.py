from django.db import models
from base.models import BaseModel

# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    long = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class District(models.Model):
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division,default=1,
                                on_delete=models.CASCADE,
                                related_name='districts')
    bn_name= models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    long = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
class Area(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District,default=1, 
                                 on_delete=models.CASCADE,
                                 related_name='areas')
    bn_name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
    
class StoreLocation(models.Model):
    name = models.CharField(max_length=100,null=True)
    area = models.ForeignKey(Area,
                             default=1,
                             on_delete=models.CASCADE,
                             related_name='store_locations')
    bn_name = models.CharField(max_length=100,null=True)

    store_location = models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return self.name