from rest_framework import viewsets,pagination
from .serializers import HotelSerializer
from .models import Hotel

class HotelPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
   
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    pagination_class = HotelPagination


    def get_queryset(self):

        queryset = super().get_queryset()

        max_price = self.request.query_params.get('max_price')
        min_price = self.request.query_params.get('min_price')
        city = self.request.query_params.get('city')
        country = self.request.query_params.get('country')
        is_available = self.request.query_params.get('available')

        if max_price:
            queryset = queryset.filter(price_per_night__lte=max_price)
        if min_price:
            queryset = queryset.filter(price_per_night__gte=min_price) 
        if city:
            queryset = queryset.filter(city=city)
        if country:
            queryset = queryset.filter(country=country)
        if is_available:
            queryset = queryset.filter(is_available=True)

        return queryset
