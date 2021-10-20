from PruebasCovidApp.models.test import User
from rest_framework import serializers
from PruebasCovidApp.models import user

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = [ 'id', 'username', 'password', 'name', 'lastname', 'age', 'gender' ]

        def create(self, validated_data):
           userInstance = User.objects.create(**validated_data)
           return userInstance 
        
        def to_representation (self, obj ):
            user =  User.objects.get(id = obj.id)
            return {
                "id": user.id,
                "username": user.username,
                "name": user.name,
                "lastname": user.lastname,
                "age": user.age,
                "gender": user.gender
            }
