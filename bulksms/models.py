from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class AutoMarkMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=30, null=True)
    message = models.CharField(max_length=320,null=True)
    date = models.DateField(null=True, blank=True)
    msgcount = models.IntegerField(null=True, blank=True)
    custcount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.description

class AutoFastMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=30, null=True)
    message = models.CharField(max_length=320,null=True)
    date = models.DateField(null=True, blank=True)
    msgcount = models.IntegerField(null=True, blank=True)
    custcount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.description

class WinPartsMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=30, null=True)
    message = models.CharField(max_length=320,null=True)
    date = models.DateField(null=True, blank=True)
    msgcount = models.IntegerField(null=True, blank=True)
    custcount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.description
    
class AutoFastTotal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=30, null=True)
    message = models.CharField(max_length=320,null=True)
    date = models.DateField(null=True, blank=True)
    msgcount = models.IntegerField(null=True, blank=True)
    custcount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.description

class CorpMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=30, null=True)
    message = models.CharField(max_length=320,null=True)
    date = models.DateField(null=True, blank=True)
    msgcount = models.IntegerField(null=True, blank=True)
    custcount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.description
