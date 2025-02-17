from rest_framework import serializers

from animals.models import Animals


class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = '__all__'