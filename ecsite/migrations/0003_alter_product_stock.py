# Generated by Django 5.1.4 on 2024-12-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecsite", "0002_rename_productpictures_productpicture_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="stock",
            field=models.PositiveIntegerField(default=0, verbose_name="在庫"),
        ),
    ]
