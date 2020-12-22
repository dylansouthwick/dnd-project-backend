from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClassViewSet, RaceViewSet, CharacterViewSet, ItemViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'races', RaceViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'items', ItemViewSet)
urlpatterns = router.urls

