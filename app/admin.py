from django.contrib import admin
from app.models import Todo

class TodoAdmin(admin.ModelAdmin):
  list_display = ("title", "description", "completed")

admin.site.register(Todo, TodoAdmin)
