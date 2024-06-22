from rest_framework import serializers
from .models import Hotel, Review

# Define HotelSerializer
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_comment(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment cannot be empty.")
        if len(value) < 10:
            raise serializers.ValidationError("Comment must be at least 10 characters long.")
        return value
    
    def validate_hotel_id(self, value):
        if not Hotel.objects.filter(id=value).exists():
            raise serializers.ValidationError(f"Hotel with id {value} does not exist.")
        return value