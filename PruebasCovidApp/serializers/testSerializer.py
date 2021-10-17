from PruebasCovidApp.models.test import Test
from rest_framework import serializers

class TestSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Test
        fields = [ 'type', 'result', 'date']

    def create(self, validated_data):
           testInstance = Test.objects.create(**validated_data)
           return testInstance 
        
    def to_representation (self, obj ):
        test =  Test.objects.get(id = obj.id)
        return {
            "id": test.id,
            "type": test.type,
            "result'": test.result,
            "date": test.date,
        }