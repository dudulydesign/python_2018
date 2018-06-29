from .models import TakeleaveEntry
from main.models import StaffRelatedEntry

def get_user_takeleave_queryset(user_id):
  staff_entries = list(StaffRelateEntry.objects.filter(user_id=user_id).all())
  staff_user_ids = [s.staff_user_id for s in staff_entries]
  print "staff_user_ids", staff_user_ids

  qs = TakeleaveEntry.objects
  qs = qs.filter(status=STATUS_WAIT)
  qs = qs.filter(user_id__in=staff_user_ids)
  qs = qs.order_by("-pub_date")

  return os
