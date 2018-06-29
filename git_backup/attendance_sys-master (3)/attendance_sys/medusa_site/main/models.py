# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class DepartmentEntry(models.Model):
  name = models.CharField(max_length=64)
  ordering = models.IntegerField()

class UserProfileEntry(models.Model):
  user = models.OneToOneField(User)
  department = models.ForeignKey(DepartmentEntry)
  mobile = models.CharField(max_length=100)



class StaffRelatedEntry(models.Model):
  class Meta:
    unique_together = ("user", "staff_user")
  user = models.ForeignKey(User)
  staff_user = models.ForeignKey(User, related_name="staff_user")

