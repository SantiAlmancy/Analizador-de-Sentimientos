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
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateHotelView(APIView):
    def post(self, request):
        data = request.data
        
        if not isinstance(data, list):
            return Response({"message": "Invalid data format", "detail": "Expected a list of hotel objects."}, status=status.HTTP_400_BAD_REQUEST)

        errors = []
        created_hotels = []

        for hotel_data in data:
            hotel_id = hotel_data.get('hotel_id')
            hotel_class = hotel_data.get('hotel_class')

            # Check if hotel_id already exists
            if Hotel.objects.filter(hotel_id=hotel_id).exists():
                errors.append({"message": "Unable to create hotel", "detail": f"Hotel with id {hotel_id} already exists."})
                continue

            serializer = HotelSerializer(data={"hotel_id": hotel_id, "hotel_class": hotel_class})
            if serializer.is_valid():
                serializer.save()
                created_hotels.append(serializer.data)
            else:
                errors.append(serializer.errors)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Hotels created successfully", "hotels": created_hotels}, status=status.HTTP_201_CREATED)