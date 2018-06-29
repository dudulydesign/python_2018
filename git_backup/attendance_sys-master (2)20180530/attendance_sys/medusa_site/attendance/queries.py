from .models import OvertimeEntry
from .consts import *
from main.models import StaffRelatedEntry

def get_user_overtime_queryset(user_id):
  staff_entries = list(StaffRelatedEntry.objects.filter(user_id=user_id).all())
  staff_user_ids = [s.staff_user_id for s in staff_entries]
  print "staff_user_ids", staff_user_ids

  qs = OvertimeEntry.objects
  qs = qs.filter(status=STATUS_WAIT)
  #qs = qs.exclude(user_id=request.user.id)
  qs = qs.filter(user_id__in=staff_user_ids)
  #qs = qs.exclude(status=STATUS_CANCEL)
  qs = qs.order_by("-pub_date")

  return qs
