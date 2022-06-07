from django.conf import settings
from .models import errorLog
import traceback
import sys


class ExceptionLoggingMiddleware:
    """
    This middleware provides saving of exceptions and stack trace in DB.
    """

    def __init__(self, get_response):
        """
        Initialization
        """

        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before
         the view (and later middleware) are called.
        """

        response = self.get_response(request)

        if response.status_code in settings.ERROR_CODE:
            response.status_code = 200
            response.reason_phrase = "Error"

        return response

    def process_exception(self, request, exception):
        """
        Processes exceptions during handling of a http request.
        saves them in Database.
        """
        
        _, _, stacktrace = sys.exc_info()

        error_stack = ''.join(traceback.format_tb(stacktrace))
        entry = errorLog(exception=exception, path=request.path , error_stack=error_stack)
        entry.save()

        return None