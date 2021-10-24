from rest_framework import generics, status
from rest_framework.response import Response
from PruebasCovidApp.serializers.testSerializer import TestSerializer

class TestCreateView(generics.CreateAPIView):
    def post (self, request, *args, **kwargs):
        serializer =  TestSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response("Transaccion exitosa", status = status.HTTP_201_CREATED)