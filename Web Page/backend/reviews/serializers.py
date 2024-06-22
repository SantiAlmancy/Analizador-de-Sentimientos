from rest_framework import serializers

class HotelSerializer(serializers.Serializer):
    hotel_id = serializers.CharField(max_length=100)
    hotel_name = serializers.CharField(max_length=255)
    hotel_class = serializers.FloatField()

    def validate_hotel_name(self, value):
        if not value:
            raise serializers.ValidationError("Hotel name cannot be empty.")
        return value

    def validate_hotel_class(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Hotel class must be between 1 and 5.")
        return value

class ReviewSerializer(serializers.Serializer):
    hotel_id = serializers.CharField(max_length=100)
    review_id = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=255)
    review = serializers.CharField()

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_review(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Review must be at least 10 characters long.")
        return value
