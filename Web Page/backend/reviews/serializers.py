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
        fields = ('review_id', 'hotel', 'title', 'review', 'value')

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_review(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Review must be at least 10 characters long.")
        return value

    def validate_value(self, value):
        if value not in ['positive', 'negative']:
            raise serializers.ValidationError("Value must be either 'positive' or 'negative'.")
        return value
