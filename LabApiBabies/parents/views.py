from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from parents.models import Parent
from babies.models import Baby

from parents.serializers import ParentSerializer
from babies.serializers import BabySerializer

# Create your views here.
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    # /parents/id/babies/
    @action(detail=True, methods=['get'])
    def babies(self, request, pk = None):
        parent = self.get_object()
        allBabies = []
        for baby in Baby.objects.filter(parent=parent):
            allBabies.append(BabySerializer(baby).data)
        return Response(allBabies)