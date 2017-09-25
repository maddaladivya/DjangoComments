# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from mail.models import Email_details, Reply

admin.site.register(Email_details)
admin.site.register(Reply)