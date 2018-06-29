

def init_overtime():
  from attendance.models import Department

  overtime_department = {
    1: {"name": u"IT"},
    2: {"name": u"HR"},
      }

  for id, item in overtime_department.items():
    try:
      over = Department.objects.get(id=id)
    except Department.DoesNotExist:
      over = Department(id=id, ordering=0)

    over.name = item["name"]
    over.save()
    print "save overtime department=%s name=%s" % (over.id, over.name)
 
def init_takeleave():
  from takeleave.models import Category
  from takeleave.models import Department

  takeleave_categories = {
    1: {"name": u"病假"},
    2: {"name": u"公假"},
    3: {"name": u"事假"},
    5: {"name": u"喪假"},
    6: {"name": u"婚假"},
    7: {"name": u"特休"},
    8: {"name": u"其它"},
      }

  for id, item in takeleave_categories.items():
    try:
      cat = Category.objects.get(id=id)
    except Category.DoesNotExist:
      cat = Category(id=id, ordering=0)

    cat.name = item["name"]
    cat.save()
    print "save takeleave category=%s name=%s" % (cat.id, cat.name)

  takeleave_department = {
    1: {"name": u"IT"},
    2: {"name": u"HR"},
      }

  for id, item in takeleave_department.items():
    try:
      dep = Department.objects.get(id=id)
    except Department.DoesNotExist:
      dep = Department(id=id, ordering=0)

    dep.name = item["name"]
    dep.save()
    print "save takeleave department=%s name=%s" % (dep.id, dep.name)


def init_test_users():
  from django.contrib.auth.models import User


  for i in range(10):
    username="testuser%s" % str(i).zfill(2)

    try:
      u = User.objects.get(username=username)
    except User.DoesNotExist:
      u = User(
          username=username,
          is_active=True
          )

    u.set_password("12345678")
    u.save()
    print "new user=%s" % username

def main():
  import random
  import uuid
  import time
  from datetime import datetime, timedelta
  from django.utils import timezone

  init_test_users()
  init_takeleave()
