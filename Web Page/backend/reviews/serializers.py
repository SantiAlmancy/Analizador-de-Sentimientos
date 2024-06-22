# reviews/serializers.py
from rest_framework import serializers
from .models import Hotel, Review

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_id', 'hotel_name', 'hotel_class')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('review_id', 'hotel_id', 'title', 'review')
