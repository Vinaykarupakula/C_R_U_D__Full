from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from app1.models import SpaceDb


class SpaceDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceDb
        fields = "__all__"