from rest_framework import viewsets

from main_app.models import Student
from main_app.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """ViewSet for Student model."""

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
