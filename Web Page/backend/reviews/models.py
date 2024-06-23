# reviews/models.py
from django.db import models

class Hotel(models.Model):
    hotel_id = models.CharField(max_length=10, primary_key=True)
    hotel_name = models.CharField(max_length=100, unique=True)
    hotel_class = models.FloatField()

    def __str__(self):
        return self.hotel_name

class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=255)
    review = models.TextField()
    value = models.CharField(max_length=10, choices=[('positive', 'Positive'), ('negative', 'Negative')])

    def __str__(self):
        return self.title

