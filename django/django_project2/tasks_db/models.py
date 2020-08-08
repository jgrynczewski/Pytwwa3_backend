from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=120, null=True)

    def __str__(self):
        return f"{self.text}"