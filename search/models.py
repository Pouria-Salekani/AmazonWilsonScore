from django.db import models



class Global_Rating(models.Model):
    total_rating = models.CharField(max_length=50)
    stars = models.CharField(max_length=10)
    whole_item = models.JSONField(default=dict)


class Bounds(models.Model):
    bounds = models.JSONField()