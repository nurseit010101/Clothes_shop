from dataclasses import field
from rest_framework import serializers


from mealapp.models import *




class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = "__all__"