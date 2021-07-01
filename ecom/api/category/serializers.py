from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"  # all the fields are serialized

