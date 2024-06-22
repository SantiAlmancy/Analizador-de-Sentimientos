from django.db import models

class Hotel(models.Model):
    hotel_id = models.CharField(max_length=10, primary_key=True)
    hotel_name = models.CharField(max_length=100, unique=True)
    hotel_class = models.FloatField()

    def __str__(self):
        return self.hotel_name

class Review(models.Model):
    review_id = models.CharField(max_length=10, primary_key=True)
    hotel = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return self.title
