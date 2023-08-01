from django.urls import include, path
from rest_framework import routers
from hotel.views import HotelViewSet

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
