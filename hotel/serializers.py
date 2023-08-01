from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

    def validate(self, data):
        price_per_night = data.get('price_per_night', None)

        if price_per_night and price_per_night < 0:
            raise serializers.ValidationError({"price_per_night":"Price per night cannot be negative."})

        return data