# Generated by Django 5.0.6 on 2024-06-23 03:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="hotel",
            new_name="hotel_id",
        ),
    ]