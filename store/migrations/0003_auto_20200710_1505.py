# Generated by Django 2.2.2 on 2020-07-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
