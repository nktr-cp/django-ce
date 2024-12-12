# Generated by Django 5.1.4 on 2024-12-11 08:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="商品名")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("cakes", "生菓子"),
                            ("bakedcakes", "焼き菓子"),
                            ("goods", "備品"),
                        ],
                        max_length=20,
                        verbose_name="種類",
                    ),
                ),
                ("price", models.IntegerField(verbose_name="価格")),
                ("stock", models.IntegerField(verbose_name="在庫")),
                ("comments", models.CharField(max_length=100, verbose_name="商品説明")),
                ("size", models.CharField(max_length=50, verbose_name="サイズ")),
                (
                    "campaign",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="キャンペーン説明"
                    ),
                ),
                ("ingredients", models.CharField(max_length=50, verbose_name="原材料")),
            ],
            options={
                "db_table": "products",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_price", models.PositiveIntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "orders",
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qty", models.PositiveIntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecsite.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ecsite.product",
                    ),
                ),
            ],
            options={
                "db_table": "order_items",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("product", "order"), name="order_constrain"
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qty", models.PositiveIntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ecsite.product"
                    ),
                ),
            ],
            options={
                "db_table": "cart_items",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("product", "user"), name="incart_product"
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name="ProductPictures",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("picture", models.FileField(upload_to="product_pictures")),
                ("priority", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ecsite.product"
                    ),
                ),
            ],
            options={
                "db_table": "product_pictures",
                "ordering": ["priority"],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("product", "priority"), name="picture_priority"
                    )
                ],
            },
        ),
    ]
