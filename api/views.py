from .models import Task
from .serializer import TaskSerializer
from rest_framework.viewsets import ModelViewSet

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()