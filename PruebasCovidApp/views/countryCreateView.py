from rest_framework import serializers, status, views
from rest_framework import response
from PruebasCovidApp.serializers.countrySerializer import CountrySerializer

class UserCreateView(views.APIview):
    def post (self, request, *args, **kwargs):
        serializer =  CountrySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()