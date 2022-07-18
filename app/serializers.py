from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from app.models import Todo

class TodoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Todo
    fields = ('id', 'title','description','completed')

    