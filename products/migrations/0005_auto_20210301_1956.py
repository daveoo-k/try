# Generated by Django 3.1.7 on 2021-03-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210226_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.BooleanField(default=False),
        ),
    ]