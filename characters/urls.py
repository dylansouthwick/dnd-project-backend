from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClassViewSet, RaceViewSet, CharacterViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'classes', ClassViewSet, basename='classes')
router.register(r'races', RaceViewSet, basename='races')
router.register(r'characters', CharacterViewSet, basename='character')
urlpatterns = router.urls

