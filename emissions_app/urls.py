from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmissionsViewSet

router = DefaultRouter()
router.register(r'emissions', EmissionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]