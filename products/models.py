from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField('Имя', max_length=100)
    description = RichTextField('Описание', blank=True, null=True, max_length=2000, help_text='Не больше 2000 символов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField('Имя', max_length=100)
    description = RichTextField('Описание', blank=True, null=True, max_length=2000, help_text='Не больше 2000 символов')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=1)
    quantity = models.PositiveIntegerField('Количество', default=0)
    image = models.ImageField('Изображение', upload_to='products/' )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

