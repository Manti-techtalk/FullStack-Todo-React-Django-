from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from api.models import Task
from api.serializers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

def apiSite(request):
    return HttpResponse ('<h1>Test Test</h1>')