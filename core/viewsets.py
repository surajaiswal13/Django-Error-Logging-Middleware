from rest_framework import viewsets
from .models import errorLog
from .serializers import ErrorLogSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

class ErrorLogViewSet(viewsets.ModelViewSet):

    """
    ModelViewSet for ErrorLogs
    """
    queryset = errorLog.objects.all()
    serializer_class = ErrorLogSerializer
    filter_backends = [SearchFilter]
    search_fields = ['exception', 'path']
