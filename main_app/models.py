from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    store_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
