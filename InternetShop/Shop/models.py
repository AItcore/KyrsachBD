from django.conf import settings
from django.db import models

# Create your models here.purchase


class Product(models.Model):
    price = models.FloatField(verbose_name="Цена")
    manufacturer = models.CharField(max_length=100, verbose_name="Производитель")
    category = models.CharField(max_length=50, verbose_name="Категория")
    Subcategory = models.CharField(max_length=100, default=None, verbose_name="Подкатегория")
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    rating = models.FloatField(verbose_name="Рейтинг")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Image(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_product = models.ImageField(null=True, blank=True,
                              upload_to='images/', verbose_name='Изображение')
    main_image = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Feedback(models.Model):
    rating = models.SmallIntegerField(verbose_name="Рейтинг")
    id_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Имя пользователя"
    )
    text = models.TextField(verbose_name="Текст отзыва")
    date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Дата добавления")
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Название продукта")

    def __str__(self):
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Purchase(models.Model):
    id_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    id_product = models.ForeignKey(Product,default=None, on_delete=models.CASCADE)
    data_purchase = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.BooleanField(default=None)

    def __str__(self):
        return f"{self.id_user} {self.id_product} {self.data_purchase}"
