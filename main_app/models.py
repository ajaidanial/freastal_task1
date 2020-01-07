from django.db import models
from django.utils import timezone


class Student(models.Model):
    """Base model for the app."""

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    standard = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
