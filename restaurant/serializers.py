from rest_framework import serializers
from .models import Menu, Booking
# from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        # fields = ['url', 'username', 'email', 'groups']
        fields = '__all__'
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
