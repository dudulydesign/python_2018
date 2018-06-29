from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
  name = models.CharField(max_length=100)
  ordering = models.IntegerField()

  def __unicode__(self):
    return self.name


class OvertimeEntry(models.Model):
  user = models.ForeignKey(User)
  department = models.ForeignKey(Department)
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

