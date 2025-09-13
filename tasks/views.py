from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_done = not instance.is_done
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
