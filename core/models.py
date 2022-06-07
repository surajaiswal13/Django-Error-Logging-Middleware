from django.db import models

# Create your models here.

class errorLog(models.Model):
    """
    Model for saving Error Logs
    """

    exception = models.CharField(max_length=800)
    path = models.CharField(max_length=500)
    error_stack = models.CharField(null=False, max_length=10000)    