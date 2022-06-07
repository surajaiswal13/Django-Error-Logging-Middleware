from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = f"<center> <h2> Hello, Please visit <a href=http://127.0.0.1:8000/error-logs> http://127.0.0.1:8000/error-logs </a>" \
            f" for more information about logs </h2> </center>"
    return HttpResponse(text)