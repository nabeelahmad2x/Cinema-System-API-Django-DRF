from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CinemaHallViewSet

router = DefaultRouter()
router.register(r'cinemahalls', CinemaHallViewSet, basename='cinemahalls')


urlpatterns = [
    path('', include(router.urls)),
]
