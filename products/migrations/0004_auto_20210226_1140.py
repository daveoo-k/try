# Generated by Django 3.1.7 on 2021-02-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True, default='this is my product buy it'),
        ),
    ]
