# Generated by Django 4.2.2 on 2023-06-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_item_price_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ItemImages/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.ManyToManyField(blank=True, null=True, related_name='prices', to='shop.price'),
        ),
    ]
