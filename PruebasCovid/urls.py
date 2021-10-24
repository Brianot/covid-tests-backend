from django.contrib import admin
from django.urls import path
from PruebasCovidApp import views 
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('test/', views.TestCreateView.as_view()),
    path('test/<int:pk>/', views.TestDetailView.as_view()),
    path('test/all/', views.TestGetAllView.as_view()),
    path('country/', views.CountryCreateView.as_view()),
    path('user/<int:pk>/',views.UserDetailView.as_view()),
]
