# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from .models import StaffRelatedEntry


admin.site.unregister(User)

class StaffRealtedInline(admin.TabularInline):
  model = StaffRelatedEntry
  fk_name = "user"

class UserAdmin(_UserAdmin):

  inlines = [StaffRealtedInline]


admin.site.register(User, UserAdmin)

# Register your models here.
