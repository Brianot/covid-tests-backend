from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from PruebasCovidApp.models.user import User
from PruebasCovidApp.serializers.userSerializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get ('HTTP_AUHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORIM'])
        valid_data = token_backend.decode(token, verify=False)

        if valid_data ['user_id'] != kwargs['pk']:
            string_response= {'detail': 'Acceso no autorizado'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)

        
