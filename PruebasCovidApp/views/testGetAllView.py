from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from PruebasCovidApp.models.test import Test
from PruebasCovidApp.serializers.testSerializer import TestSerializer


class TestGetAllView(generics.ListAPIView):
    serializer_class = TestSerializer
    permission_class = [IsAuthenticated,]

    def get_queryset(self):
        queryset = Test.objects.all()
        return queryset

