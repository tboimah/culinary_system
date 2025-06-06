# Generated by Django 5.1.6 on 2025-06-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0006_order_items"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Preparing", "Preparing"),
                    ("Completed", "Completed"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
    ]
