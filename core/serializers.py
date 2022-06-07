from rest_framework import serializers
from .models import errorLog

class ErrorLogSerializer(serializers.ModelSerializer):
    """
    Serializer for ErrorLogs
    """

    class Meta:
        model = errorLog
        fields = ('id', 'exception', 'path', 'error_stack')