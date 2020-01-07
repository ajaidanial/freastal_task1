from rest_framework import serializers

from main_app.models import Student


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for the Student model."""

    class Meta:
        model = Student
        fields = "__all__"
