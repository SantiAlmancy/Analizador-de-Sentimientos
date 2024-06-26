from django.urls import path
from .views import HotelListView, HotelReviewListView, CreateReviewView, CreateHotelView, HuggingFacePredictionView, KerasModelPredictionView

urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotel-list'), # Endpoint: list all hotels
    path('hotels/<str:hotel_id>/reviews/', HotelReviewListView.as_view(), name='hotel-review-list'), # Endpoint: list all reviews of specific hotel
    path('reviews/', CreateReviewView.as_view(), name='create-review'), # Endpoint: Create new review for specific hotel
    path('hotels/add/', CreateHotelView.as_view(), name='create-hotel'),  # Endpoint: Create new hotels from a list
    path('transformer-predict/', HuggingFacePredictionView.as_view(), name='transformer-model-predict'), # Endpoint: Predict review value and create new review (Transformer)
    path('keras-predict/', KerasModelPredictionView.as_view(), name='keras-model-predict'), # Endpoint: Predict review value and create new review (LSTM)
]
