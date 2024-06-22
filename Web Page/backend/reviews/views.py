from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HotelSerializer, ReviewSerializer

# Simulated in-memory data
hotels_data = [
    {'hotel_id': '1', 'hotel_name': 'Hotel A', 'hotel_class': 4.5},
    {'hotel_id': '2', 'hotel_name': 'Hotel B', 'hotel_class': 3.8},
    # Add more sample data as needed
]
reviews_data = [
    {'review_id': '101', 'hotel_id': '1', 'title': 'Great stay', 'review': 'Really enjoyed my stay at Hotel A.'},
    {'review_id': '102', 'hotel_id': '2', 'title': 'Not bad', 'review': 'Hotel B was okay, but could be better.'},
    # Add more sample data as needed
]

class HotelListView(APIView):
    def get(self, request):
        serializer = HotelSerializer(hotels_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HotelReviewListView(APIView):
    def get(self, request, hotel_id):
        try:
            hotel = next((hotel for hotel in hotels_data if hotel['hotel_id'] == hotel_id), None)
            if not hotel:
                return Response({"message": "Unable to retrieve reviews", "detail": f"Hotel with id {hotel_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
            
            reviews = [review for review in reviews_data if review['hotel_id'] == hotel_id]
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Unable to retrieve reviews", "detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer
import uuid  # For generating unique review_id

class CreateReviewView(APIView):
    def post(self, request):
        hotel_id = request.data.get('hotel_id')
        review_title = request.data.get('review_title')
        review_review = request.data.get('review_review')

        # Validate hotel_id exists
        hotel = next((hotel for hotel in hotels_data if hotel['hotel_id'] == hotel_id), None)
        if not hotel:
            return Response({"message": "Hotel not found"}, status=status.HTTP_404_NOT_FOUND)

        # Validate review_title and review_review are not empty (additional validations can be added)
        if not review_title or not review_review:
            return Response({"message": "Title and review content are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a unique review_id
        review_id = str(uuid.uuid4())  # Using UUID for simplicity and uniqueness

        # Create new review
        new_review = {
            'hotel_id': hotel_id,
            'title': review_title,
            'review': review_review,
            'review_id': review_id
        }

        # Add the new review to reviews_data (assuming reviews_data is a list of dicts)
        reviews_data.append(new_review)

        # Serialize and return the new review
        serializer = ReviewSerializer(new_review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
