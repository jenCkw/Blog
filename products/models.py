from django.db import models
import uuid

class Category(models.Model):
    name = models.CharField(max_length=200)



class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    last_modification = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(null=True)
    category = models.ForeignKey(Category, models.PROTECT, null=True)

    def __str__(self):
        return self.name + " " + "(" +  str(self.price) + ")"
    