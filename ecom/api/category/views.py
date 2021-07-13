from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
# we need our model
from .models import Category
# importing the corresponding serializer
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """specifying the query to pull all the Category model data"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
