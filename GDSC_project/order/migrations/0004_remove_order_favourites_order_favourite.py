# Generated by Django 4.1.7 on 2023-03-25 09:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("order", "0003_order_favourites"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="favourites",
        ),
        migrations.AddField(
            model_name="order",
            name="favourite",
            field=models.ManyToManyField(
                blank=True, related_name="favourite", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]