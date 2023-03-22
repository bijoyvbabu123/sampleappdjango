from django.db import models

# Create your models here.

# model for storing cat names
class CatName(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
        