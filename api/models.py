from django.db import models

# Create your models here.
class itemModel(models.Model):
    item = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    