# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app.models import *

admin.site.register(Consumer)
admin.site.register(Organisation)
admin.site.register(Business)
admin.site.register(Badge)
admin.site.register(BadgeClaim)


# Register your models here.
