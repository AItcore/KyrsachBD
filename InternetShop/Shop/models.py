from django.conf import settings
from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField()


class Product(models.Model):
    price = models.FloatField()
    manufacturer = models.CharField(max_length=100)
    id_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Feedback(models.Model):
    rating = models.SmallIntegerField()
    id_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.text) > 50:
            return self.text
        else:
            return self.text[50:] + "..."


class Purchase(models.Model):
    id_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    data_purchase = models.DateTimeField(auto_now_add=True)
