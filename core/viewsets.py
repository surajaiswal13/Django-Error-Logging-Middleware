from rest_framework import viewsets
from .models import errorLog
from .serializers import ErrorLogSerializer
from rest_framework.response import Response

class ErrorLogViewSet(viewsets.ViewSet):

    """
    ViewSet for ErrorLogs
    """

    def list(self, request):
        queryset = errorLog.objects.all()
        serializer = ErrorLogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = errorLog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ErrorLogSerializer(user)
        return Response(serializer.data)