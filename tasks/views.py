from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Les méthodes pour les opérations CRUD (Create, Read, Update, Delete) sont déjà gérées par ModelViewSet.
