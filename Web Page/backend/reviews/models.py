from django.db import models

class Hotel(models.Model):
    hotel_id = models.IntegerField()
    hotel_name = models.CharField(max_length=255)
    hotel_class = models.IntegerField()

class Review(models.Model):
    review_hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_id = models.IntegerField()