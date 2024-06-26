from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel, Review
from .serializers import HotelSerializer, ReviewSerializer
from .predictionModels import Model

# Create an instance of Model
models = Model()

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
            hotel_name = hotel_data.get('hotel_name')
            hotel_class = hotel_data.get('hotel_class')

            # Check if hotel_id already exists
            if Hotel.objects.filter(hotel_id=hotel_id).exists():
                errors.append({"message": "Unable to create hotel", "detail": f"Hotel with id {hotel_id} already exists."})
                continue

            serializer = HotelSerializer(data={"hotel_id": hotel_id, "hotel_name": hotel_name, "hotel_class": hotel_class})
            if serializer.is_valid():
                serializer.save()
                created_hotels.append(serializer.data)
            else:
                errors.append(serializer.errors)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Hotels created successfully", "hotels": created_hotels}, status=status.HTTP_201_CREATED)

class HuggingFacePredictionView(APIView):
    def post(self, request):
        text = request.data.get("text", "")
        hotel_id = request.data.get("hotel_id", "")

        if not text or not hotel_id:
            return Response({"error": "Text and hotel_id are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            hotel = Hotel.objects.get(hotel_id=hotel_id)
        except Hotel.DoesNotExist:
            return Response({"error": "Hotel does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Preprocess text and get prediction
        processed_text = models.preprocess_text(text)
        prediction = models.classifier(processed_text, return_all_scores=True)
        # Map predicted label
        predicted_label = models.mapLabels(prediction).lower()
        # Create Review object
        review_data = {
            "hotel": hotel,
            "review": text,
            "value": predicted_label
        }
        review_instance = Review.objects.create(**review_data)
        serializer = ReviewSerializer(review_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class KerasModelPredictionView(APIView):
    def post(self, request):
        text = request.data.get("text", "")
        hotel_id = request.data.get("hotel_id", "")

        if not text or not hotel_id:
            return Response({"error": "Missing required fields: text and hotel_id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            hotel = Hotel.objects.get(hotel_id=hotel_id)
        except Hotel.DoesNotExist:
            return Response({"error": f"Hotel with ID {hotel_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        # Preprocess text and get prediction label
        pred = models.predict_text(text).lower()
        # Create Review object
        review_data = {
            "hotel": hotel,
            "review": text,
            "value": pred
        }
        review_instance = Review.objects.create(**review_data)
        serializer = ReviewSerializer(review_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)