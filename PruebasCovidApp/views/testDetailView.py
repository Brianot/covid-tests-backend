from django.conf import settings
from rest_framework import generics
from PruebasCovidApp.models.test import Test
from PruebasCovidApp.serializers.testSerializer import TestSerializer


class TestDetailView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    def get(self, request, *args, **kwargs):
        return  super().get(request, *args, **kwargs)

   