# Generated by Django 4.1.7 on 2023-03-25 09:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("order", "0002_order_time_posted"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="favourites",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                related_name="favourite",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
