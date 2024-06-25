# Generated by Django 5.0.6 on 2024-06-24 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_review_title_alter_review_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('positive', 'Positive'), ('very_positive', 'Very Positive'), ('neutral', 'Neutral'), ('negative', 'Negative'), ('very_negative', 'Very Negative')], max_length=20),
        ),
    ]
