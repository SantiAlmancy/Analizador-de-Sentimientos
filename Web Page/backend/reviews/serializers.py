from rest_framework import serializers

# Sample data (would be in your database in a real application)
hotels = [
    {"id": 1, "name": "Hotel California"},
    {"id": 2, "name": "Grand Budapest Hotel"}
]

class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # Make id read-only
    hotel_id = serializers.IntegerField()
    comment = serializers.CharField(max_length=1024)
    
    def validate_comment(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment cannot be empty.")
        if len(value) < 10:
            raise serializers.ValidationError("Comment must be at least 10 characters long.")
        return value
    
    def validate_hotel_id(self, value):
        if not any(hotel['id'] == value for hotel in hotels):
            raise serializers.ValidationError(f"Hotel with id {value} does not exist.")
        return value
