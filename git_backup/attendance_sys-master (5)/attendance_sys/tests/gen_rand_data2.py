

def main():
  import random
  import uuid
  import time
  from datetime import datetime, timedelta
  from django.contrib.auth.models import User
  from django.utils import timezone
  from takeleave.models import TakeleaveEntry
  from takeleave.models import Department
  from faker import Faker

  random.seed(datetime.now())

  fake = Faker()
  fake_zh = Faker("zh-tw")

  """
  for i in xrange(3):
    username = "%s%s" % (fake.name().replace(' ', ''), int(time.time()))
    user = User(
      username=username,
      is_active=True
      )
    user.set_password("12345678")
    user.save()
    print "create user", user.id, user.username
  """

  all_users = list(User.objects.all())

  now = timezone.now()

  for i in xrange(100):
    user = random.choice(all_users)
    start_time = now - timedelta(minutes=random.randint(1, 2**16))
    end_time = start_time + timedelta(minutes=random.randint(1, 600))
    entry = TakeleaveEntry(
      user=user,
      status=0,
      department=department,
      start_time=start_time,
      end_time=end_time,
      pub_date=timezone.now(),
      reason=fake_zh.text()
      )
    entry.save()

    print "create takeleave", entry.id, entry.user_id, entry.start_time

