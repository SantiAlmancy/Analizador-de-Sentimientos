from django.urls import path
from .views import HotelListView, HotelReviewListView, CreateReviewView

urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/<int:hotel_id>/reviews/', HotelReviewListView.as_view(), name='hotel-review-list'),
    path('reviews/', CreateReviewView.as_view(), name='create-review'),
]
