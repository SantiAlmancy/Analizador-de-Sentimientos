from rest_framework import serializers
from .models import Hotel, Review

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_id', 'hotel_name', 'hotel_class')

class ReviewSerializer(serializers.ModelSerializer):
    hotel_id = serializers.RegexField(regex=r'^H\d{5}$', error_messages={'invalid': 'Hotel ID must be in the format H00001'})

    class Meta:
        model = Review
        fields = ('hotel_id', 'review', 'value')

    def create(self, validated_data):
        hotel_id = validated_data.pop('hotel_id')  
        # Create Review object
        review = Review.objects.create(hotel_id=hotel_id, **validated_data)
        return review

    def validate_hotel_id(self, value):
        if not value:
            raise serializers.ValidationError({"hotel_id": "This field is required."})
        return value