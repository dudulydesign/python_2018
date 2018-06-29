from django.db import models
from django.contrib.auth.models import User

class OvertimeEntry(models.Model):
  user = models.ForeignKey(User)
  status = models.IntegerField()
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  reason = models.TextField()
  pub_date = models.DateTimeField()
  date_created = models.DateTimeField(auto_now_add=True)


class OvertimeApplyEntry(models.Model):
  user = models.ForeignKey(User)
  overtime = models.ForeignKey(OvertimeEntry)
  time = models.DateTimeField()
  date_created = models.DateTimeField(auto_now_add=True)

