from rest_framework import serializers, status, views
from rest_framework.response import Response
from PruebasCovidApp.serializers.countrySerializer import CountrySerializer

class CountryCreateView(views.APIView):
    def post (self, request, *args, **kwargs):
        serializer =  CountrySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status = status.HTTP_201_CREATED)