from django.db import models


# Create your models here.
class File(models.Model):
    word = models.CharField(max_length=128, default=' ')
    file = models.FileField(upload_to='files/', null=True, max_length=255)