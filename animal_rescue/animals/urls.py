from django.urls import path, include
from rest_framework.routers import DefaultRouter

from animals import views


router = DefaultRouter()
router.register('animals', views.AnimalsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]