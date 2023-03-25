from django.db import models

# Create your models here.


class Global_Rating(models.Model):
    total_rating = models.CharField(max_length=50)
    stars = models.CharField(max_length=10)