from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shows import views
router = DefaultRouter()
router.register(r'shows', views.ShowsViewSet, basename='shows')


urlpatterns = [
    path('', include(router.urls)),
]
