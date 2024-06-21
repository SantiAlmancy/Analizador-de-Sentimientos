from rest_framework import serializers

class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # Make id read-only
    hotel_id = serializers.IntegerField()
    # rating = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField(max_length=1024)
