from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HotelSerializer, ReviewSerializer
import json

# In-memory data storage
hotels = [
    {"id": 1, "name": "Hotel California"},
    {"id": 2, "name": "Grand Budapest Hotel"}
]

reviews = []

class HotelListView(APIView):
    def get(self, request):
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HotelReviewListView(APIView):
    def get(self, request, hotel_id):
        hotel_reviews = [review for review in reviews if review['hotel_id'] == hotel_id]
        serializer = ReviewSerializer(hotel_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateReviewView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            serializer = ReviewSerializer(data=data)
            if serializer.is_valid():
                review = serializer.validated_data
                review['id'] = len(reviews) + 1  # Auto-generate id
                reviews.append(review)
                return Response(review, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)
