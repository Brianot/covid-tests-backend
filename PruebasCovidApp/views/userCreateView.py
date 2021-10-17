from rest_framework import serializers, status, views
from rest_framework import response
from rest_framework_simplejwt import TokenObtainSerializer
from PruebasCovidApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIview):
    def post (self, request, *args, **kwargs):
        serializer =  UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()