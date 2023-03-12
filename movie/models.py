from django.db import models
from category.models import Category
from cloudinary.models import CloudinaryField
# Create your models here.
class Movie(models.Model):

    name = models.CharField(
        'Titles' , blank=False , null=False , max_length=20, db_index=True
    )
    address = models.CharField(
        'Sortation' , blank=False , null=False , max_length=20, db_index=True ,default='nakia' 
    )
    image = CloudinaryField(
        'Poster',blank=True ,null=True
    )

    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE 
    )
