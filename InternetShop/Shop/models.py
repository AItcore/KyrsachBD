from django.conf import settings
from django.db import models

# Create your models here.


class Product(models.Model):
    price = models.FloatField()
    manufacturer = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    Subcategory = models.CharField(max_length=100, default=None)
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Image(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_product = models.ImageField(null=True, blank=True,
                              upload_to='images/', verbose_name='Изображение')
    main_image = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


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

    def __str__(self):
        return f"{id_user}  {data_purchase}"
