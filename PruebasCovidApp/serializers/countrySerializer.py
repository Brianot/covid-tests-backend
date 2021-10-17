from PruebasCovidApp.models.country import Country
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Country
        fields = [ 'name']

    def create(self, validated_data):
           countryInstance = Country.objects.create(**validated_data)
           return countryInstance 
        
    def to_representation (self, obj ):
        country =  Country.objects.get(id = obj.id)
        return {
            "id": country.id,
            "name": country.name
        }