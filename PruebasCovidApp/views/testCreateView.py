from rest_framework import serializers, status, views
from rest_framework import response
from PruebasCovidApp.serializers.testSerializer import TestSerializer

class TestcreateView(views.APIView):
    def post (self, request, *args, **kwargs):
        serializer =  TestSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()