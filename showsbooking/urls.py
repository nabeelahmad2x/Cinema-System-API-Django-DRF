from rest_framework import routers
from django.urls import path, include

from .views import BookingViewSet


router = routers.DefaultRouter()
router.register(r'booking/', BookingViewSet, basename='booking')

# Include the router's URLs in the main urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('user_bookings/', BookingViewSet.as_view({'get': 'get_user_bookings'})),
]