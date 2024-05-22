from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.TextField(max_length=150)
    release_date = models.DateField(max_length=20)
    lte_exists = models.BooleanField()
    slug = models.SlugField()

