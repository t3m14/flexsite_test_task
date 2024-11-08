from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    # Add any other fields you need for your organization modl