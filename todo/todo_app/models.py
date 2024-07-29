from django.db import models

class Todo(models.Model):
    task=models.TextField()
    created_at=models.DateField()
    is_complete=models.BooleanField(default=False)


