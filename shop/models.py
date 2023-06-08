from django.db import models
from django.template.defaultfilters import slugify


class Item(models.Model):
    """ Item model """
    name = models.CharField(max_length=450)
    image = models.ImageField(upload_to='ItemImages/')
    slug = models.SlugField(null=True, blank=True, unique=True)
    price = models.ManyToManyField('Price', related_name='prices', null=True, blank=True)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    purpose = models.TextField(null=True, blank=True, verbose_name='Назначение')
    color = models.TextField(null=True, blank=True, verbose_name='Цвет')
    degree_of_gloss = models.TextField(null=True, blank=True, verbose_name='Степень глянца')
    warranty = models.TextField(null=True, blank=True, verbose_name='Гарантия')
    expiration_date = models.TextField(null=True, blank=True, verbose_name='Срок хранения')
    composition = models.TextField(null=True, blank=True, verbose_name='Состав')
    method_of_use = models.TextField(null=True, blank=True, verbose_name='Метод использования')
    expense = models.TextField(null=True, blank=True, verbose_name='Расход')
    flammable = models.BooleanField(null=True, blank=True, verbose_name='Огнеопасно')
    traits = models.TextField(null=True, blank=True, verbose_name='Свойства')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Price(models.Model):
    volume = models.CharField(max_length=150, null=False, verbose_name='Объем')
    bulk = models.PositiveIntegerField(null=False, verbose_name='Оптом')
    retail = models.PositiveIntegerField(null=False, verbose_name='В розницу')


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Название подраздела')

    def __str__(self):
        return self.name
