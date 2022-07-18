from rest_framework import viewsets

from app.models import Todo
from app.serializers import TodoSerializer

class TodoView(viewsets.ModelViewSet):
  serializer_class = TodoSerializer

  queryset = Todo.objects.all()

