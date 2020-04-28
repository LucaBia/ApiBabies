from django.shortcuts import render
from rest_framework import viewsets
from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory
from rest_framework.response import Response

from events.models import Event
from events.serializers import EventSerializer

def evaluate(user, obj, request):
    return user.username == obj.baby.parent.name

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permisos
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'events.view_event',
                    'destroy': evaluate,
                    'update': evaluate,
                    'partial_update': 'events.change_event',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        parent_baby = serializer.validated_data["baby"]
        user = self.request.user
        actual_user = str(user.username)
        parent = str(parent_baby)
        
        if (actual_user != parent):
            print ("No tiene autorización")
        elif(actual_user == parent):
            event = serializer.save()
            assign_perm('events.change_event', user, event)
            assign_perm('events.view_event', user, event)
            print ("Evento registrado con exito!")
            return Response(serializer.data)
