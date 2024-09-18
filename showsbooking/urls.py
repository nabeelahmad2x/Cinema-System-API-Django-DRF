
from django.urls import path
from .views import BookingView
urlpatterns = [
    path('booking/post/', BookingView.as_view(), name='booking_post'),
    path('booking/user/<int:user_id>/', BookingView.as_view(), name='booking_get'),
]
