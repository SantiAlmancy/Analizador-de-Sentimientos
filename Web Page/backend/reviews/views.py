from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel, Review
from .serializers import HotelSerializer, ReviewSerializer

class HotelListView(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()[:20]
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HotelReviewListView(APIView):
    def get(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(hotel_id=hotel_id)
            reviews = hotel.reviews.all()[:20]
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Hotel.DoesNotExist:
            return Response({"message": "Unable to retrieve reviews", "detail": f"Hotel with id {hotel_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

class CreateReviewView(APIView):
    def post(self, request):
        data = request.data
        hotel_id = data.get('hotel_id')
        review_id = data.get('review_id')
        title = data.get('title')
        review = data.get('review')
        value = data.get('value')

        try:
            hotel = Hotel.objects.get(hotel_id=hotel_id)
        except Hotel.DoesNotExist:
            return Response({"message": "Unable to create review", "detail": f"Hotel with id {hotel_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        if not title:
            return Response({"message": "Unable to create review", "detail": "Title field cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)
        if len(review) < 10:
            return Response({"message": "Unable to create review", "detail": "Review must be at least 10 characters long."}, status=status.HTTP_400_BAD_REQUEST)
        if value not in ['positive', 'negative']:
            return Response({"message": "Unable to create review", "detail": "Value must be either 'positive' or 'negative'."}, status=status.HTTP_400_BAD_REQUEST)
        if Review.objects.filter(review_id=review_id).exists():
            return Response({"message": "Unable to create review", "detail": f"Review with id {review_id} already exists."}, status=status.HTTP_400_BAD_REQUEST)

        review = Review(hotel=hotel, review_id=review_id, title=title, review=review, value=value)
        review.save()

        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
