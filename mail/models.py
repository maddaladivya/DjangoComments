# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Email_details(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    comment = models.CharField(max_length=10000)


    def __str__(self):
        return self.name
class Reply(models.Model):
    comments = models.ForeignKey(Email_details, on_delete=models.CASCADE, default=0)
    reply = models.CharField(max_length=100000, default=False)