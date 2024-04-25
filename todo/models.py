from django.db import models
from django.conf import settings


class Task(models.Model):

    class TaskPriority(models.IntegerChoices):
        LOW = 0, "Low"
        NORMAL = 1, "Normal"
        HIGH = 2, "High"

    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=256)
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField(
        default=TaskPriority.NORMAL, choices=TaskPriority.choices
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="task"
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "task"
        verbose_name = "task"

    def __str__(self):
        return self.name
