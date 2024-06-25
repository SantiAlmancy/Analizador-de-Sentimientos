from django.urls import path
from .views import HotelListView, HotelReviewListView, CreateReviewView, CreateHotelView, HuggingFacePredictionView, KerasModelPredictionView

urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/<str:hotel_id>/reviews/', HotelReviewListView.as_view(), name='hotel-review-list'),
    path('reviews/', CreateReviewView.as_view(), name='create-review'),
    path('hotels/add/', CreateHotelView.as_view(), name='create-hotel'),  # New endpoint for adding hotels
    path('transformer-predict/', HuggingFacePredictionView.as_view(), name='transformer-model-predict'),
    path('keras-predict/', KerasModelPredictionView.as_view(), name='keras-model-predict'),
]
