# reviews/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel, Review
from .serializers import HotelSerializer, ReviewSerializer

class HotelListView(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()[:20]  # Limit to 20 rows
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HotelReviewListView(APIView):
    def get(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(pk=hotel_id)
            reviews = hotel.reviews.all()[:20]  # Limit to 20 rows
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Hotel.DoesNotExist:
            return Response({"message": "Unable to retrieve reviews", "detail": f"Hotel with id {hotel_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

class CreateReviewView(APIView):
    def post(self, request):
        data = request.data
        hotel_id = data.get('hotel_id')
        comment = data.get('comment')
        text = data.get('text')

        # Validate hotel_id
        try:
            hotel = Hotel.objects.get(id=hotel_id)
        except Hotel.DoesNotExist:
            return Response({"message": "Unable to create review", "detail": f"Hotel with id {hotel_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        # Validate comment and text
        if not comment:
            return Response({"message": "Unable to create review", "detail": "Comment field cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)
        if not text:
            return Response({"message": "Unable to create review", "detail": "Text field cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save the review
        review = Review(hotel=hotel, comment=comment, text=text)
        review.save()

        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateHotelView(APIView):
    def post(self, request):
        data = request.data
        
        if not isinstance(data, list):
            return Response({"message": "Invalid data format", "detail": "Expected a list of hotel objects."}, status=status.HTTP_400_BAD_REQUEST)

        for hotel_data in data:
            hotel_id = hotel_data.get('hotel_id')
            hotel_name = hotel_data.get('hotel_name')
            hotel_class = hotel_data.get('hotel_class')

            if not hotel_name:
                return Response({"message": "Unable to create hotel", "detail": "Hotel name field cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)
            if not (1 <= hotel_class <= 5):
                return Response({"message": "Unable to create hotel", "detail": "Hotel class must be between 1 and 5."}, status=status.HTTP_400_BAD_REQUEST)
            if Hotel.objects.filter(hotel_id=hotel_id).exists():
                return Response({"message": "Unable to create hotel", "detail": f"Hotel with id {hotel_id} already exists."}, status=status.HTTP_400_BAD_REQUEST)

            hotel = Hotel(hotel_id=hotel_id, hotel_name=hotel_name, hotel_class=hotel_class)
            hotel.save()

        return Response({"message": "Hotels created successfully"}, status=status.HTTP_201_CREATED)
