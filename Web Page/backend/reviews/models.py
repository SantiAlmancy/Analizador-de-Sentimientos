from django.db import models

class Hotel(models.Model):
    hotel_id = models.CharField(max_length=10, primary_key=True)
    hotel_name = models.CharField(max_length=100, unique=True)
    hotel_class = models.FloatField()

    def __str__(self):
        return self.hotel_name

class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    value = models.CharField(max_length=20, choices = [('positive', 'Positive'), ('very_positive', 'Very Positive'), ('neutral', 'Neutral'), ('negative', 'Negative'), ('very_negative', 'Very Negative')])

    def __str__(self):
        return self.value
