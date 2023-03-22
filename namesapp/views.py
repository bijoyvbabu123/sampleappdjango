from django.shortcuts import render
from .serializers import CatNameSerializer
from .models import CatName
from rest_framework import generics

# Create your views here.

class CatNameList(generics.ListCreateAPIView):
    queryset = CatName.objects.all()
    serializer_class = CatNameSerializer
