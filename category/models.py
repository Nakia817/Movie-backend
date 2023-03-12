from django.db import models

# Create your models here.
class Category(models.Model):

    name= models.CharField(
        'Time', blank=False, null=False , max_length=15 , db_index=True
      
    )
    Date=  models.CharField(
        'Place' , blank=False, null=False , max_length=15 , db_index=True, default='nakia'
    ) 

    def __str__(self):
        return self.name