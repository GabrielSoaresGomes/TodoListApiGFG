from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.api import TodoView

router = DefaultRouter()
router.register(r"todo", TodoView, 'todo')

urlpatterns = [
    path('', include(router.urls))
]

