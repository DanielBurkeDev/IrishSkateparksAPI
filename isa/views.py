from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import SkateparkSerializer
from .models import Skateparks


class SkateParksView(viewsets.ModelViewSet):
    search_fields = ["name", "county"]
    filter_backends = (filters.SearchFilter,)
    serializer_class = SkateparkSerializer
    queryset = Skateparks.objects.all()
