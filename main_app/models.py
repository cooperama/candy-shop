from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import User, AbstractUser


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class User(AbstractUser):
#     STORE = 1
#     BUYER = 2

#     ROLE_CHOICES = (
#         (STORE, 'Store'),
#         (BUYER, 'Buyer')
#     )

#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

class Store(models.Model):
    store_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buyers = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.store_name


class Candy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=50)

    # Deleting the last candy belonging to a store deletes the store as well :(
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def in_stock(self):
        if self.stock <= 0:
            return "Out of Stock"
        elif self.stock <= 10:
            return "Limited Quantity"