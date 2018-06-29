
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  name = models.CharField(max_length=100)
  ordering = models.IntegerField()

  def __unicode__(self):
    return self.name

class Department(models.Model):
  name = models.CharField(max_length=100)
  ordering = models.IntegerField()

  def __unicode__(self):
    return self.name

class TakeleaveEntry(models.Model):
  user = models.ForeignKey(User)
  category = models.ForeignKey(Category)
  department = models.ForeignKey(Department)
  status = models.IntegerField()
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  reason = models.TextField()
  pub_date = models.DateTimeField()
  date_created = models.DateTimeField(auto_now_add=True)

class TakeleaveApplyEntry(models.Model):
  user = models.ForeignKey(User)
  takeleave = models.ForeignKey(TakeleaveEntry)
  time = models.DateTimeField()
  date_created = models.DateTimeField(auto_now_add=True)

