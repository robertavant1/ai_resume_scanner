from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=25, required = True, default=None)
    