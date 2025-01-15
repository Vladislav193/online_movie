from django.urls import path, include
from views import VideosViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'videos', VideosViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]