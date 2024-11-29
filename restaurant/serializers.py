from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, Menu, MenuItem


# written code"username", "email", "groups"]


class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
