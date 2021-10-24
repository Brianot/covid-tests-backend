from PruebasCovidApp.models.test import Test
from PruebasCovidApp.models.user import User
from PruebasCovidApp.models.country import Country
from rest_framework import serializers


class TestSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Test
        fields = ['user', 'country', 'date', 'result', 'type']

    def create(self, validated_data):
           testInstance = Test.objects.create(**validated_data)
           return testInstance 
           
        
    def to_representation (self, obj):
        usuario = User.objects.get(id = obj.user.id)
        pais = Country.objects.get(id = obj.country.id)
        test =  Test.objects.get(id = obj.id)
        
        return {
            "id": test.id,
            "type": test.type,
            "result": test.result,
            "date": test.date, 
            "user":{
                "id": usuario.id,
                "username": usuario.username,
                "name": usuario.name,
                "lastname": usuario.lastname,
                "age": usuario.age,
                "gender": usuario.gender 
            },
            "country": {
                "id": pais.id,
                "name": pais.name
            },               
        }