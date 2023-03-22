from .models import CatName

from rest_framework import serializers


# serializer for cat names
class CatNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatName
        fields = '__all__'