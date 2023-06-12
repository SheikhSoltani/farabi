from django.shortcuts import get_object_or_404
from pytils.translit import slugify

from django.db import models


class Item(models.Model):
    """ Item model """
    name = models.CharField(max_length=450)
    image = models.ImageField(upload_to='ItemImages/', null=True, blank=True)
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

    @staticmethod
    def create_item(info_dict):
        print(info_dict)
        price_objects = []
        print(info_dict['price_array'])
        print("fgh")
        for price_unit in info_dict['price_array']:
            print(price_unit)
            print(price_unit['volume'])
            print(price_unit['volume'][0])
            price_objects.append(Price.objects.create(
                volume=price_unit['volume'],
                bulk=price_unit['bulk'],
                retail=price_unit['retail']
            ))
        print('qweqwe')
        item = Item.objects.create(
            name=info_dict['name'][0],
            image=info_dict['image'][0],
            description=info_dict['description'][0],
            tag_id=int(info_dict['tag'][0]),
            purpose=info_dict['purpose'][0],
            color=info_dict['color'][0],
            degree_of_gloss=info_dict['degree_of_gloss'][0],
            warranty=info_dict['warranty'][0],
            expiration_date=info_dict['expiration_date'][0],
            composition=info_dict['composition'][0],
            method_of_use=info_dict['method_of_use'][0],
            expense=info_dict['expense'][0],
            flammable=info_dict['flammable'][0],
            traits=info_dict['traits'][0]
        )
        print(item)
        for price in price_objects:
            item.price.add(price)

    @staticmethod
    def edit_item(info_dict):
    #TODO price edit
        print(info_dict)
        item = get_object_or_404(Item, id=info_dict['id'][0])
        item.name = info_dict['name'][0]
        item.image = info_dict['image'][0]
        item.tag = get_object_or_404(Tag, id=info_dict['tag'][0])
        print("yrtguh")
        item.description = info_dict['description'][0]
        item.purpose = info_dict['purpose'][0]
        item.color = info_dict['color'][0]
        item.degree_of_gloss = info_dict['degree_of_gloss'][0]
        item.warranty = info_dict['warranty'][0]
        item.expiration_date = info_dict['expiration_date'][0]
        item.composition = info_dict['composition'][0]
        item.method_of_use = info_dict['method_of_use'][0]
        item.expense = info_dict['expense'][0]
        item.flammable = info_dict['flammable'][0]
        item.traits = info_dict['traits'][0]
        item.save()


    @staticmethod
    def delete_item(info_dict):
        try:
            item = get_object_or_404(Item, id=info_dict['id'])
            item.delete()
        except Exception as e:
            return False
        return True


class Price(models.Model):
    volume = models.CharField(max_length=150, null=False, verbose_name='Объем')
    bulk = models.PositiveIntegerField(null=False, verbose_name='Оптом')
    retail = models.PositiveIntegerField(null=False, verbose_name='В розницу')


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Название подраздела')

    def __str__(self):
        return self.name

    @staticmethod
    def create_tag(info_dict):
        print(info_dict)
        Tag.objects.create( name=info_dict['tag_name'])
        return True

    @staticmethod
    def edit_tag(info_dict):
        tag = get_object_or_404(Tag, name=info_dict['tag_name'])
        tag.name = info_dict['tag_new_name']
        tag.save()
        return True

    @staticmethod
    def delete_tag(info_dict):
        tag = get_object_or_404(Tag, name=info_dict['tag_name'])
        tag.delete()
        return True
