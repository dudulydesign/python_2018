# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url
from django.core.paginator import Paginator
from django.utils import timezone
from utils.paginations import generate_pagination
from .models import TakeleaveEntry
from main.models import StaffRelatedEntry
from django.core.exceptions import PermissionDenied
from .forms import ApplyTakeleaveForm, TakeleaveAuditForm
from .queries import get_user_takeleave_queryset


STATUS_WAIT = 0
STATUS_SUCCESS = 1
STATUS_REJECTED = 2
STATUS_CANCEL = 3

def status_to_text(status):
  if status == STATUS_WAIT:
    return u"審核中"

  if status == 1:
    return u"審核成功"

  if status == 2:
    return u"審核失敗"

  return "Nan"


  


def takeleave_audit(request):
  print "=" * 100
  print "method", request.method
  _id = int(request.GET["q"])
  entry = TakeleaveEntry.objects.get(id=_id)

  if request.method == "POST":
    form = TakeleaveAuditForm(request.POST)
    print "is_valid", form.is_valid()
    if form.is_valid():
      status = form.cleaned_data["status"]

      print "!!!> status", status
      if status == 1:
        entry.status = STATUS_SUCCESS
      else:
        entry.status = STATUS_REJECTED
      entry.save()

      print "SUCCESS!!"

      return JsonResponse({"code": 0, "msg": u"簽核成功"})
    return JsonResponse({"code": 1, "msg": str(form.errors)})

  else:
    form = TakeleaveAuditForm()
  
  return TemplateResponse(request, "attendance/takeleave_audit.html", {
    "entry": entry,
    "form": form,
    })


def takeleave_audit_list(request):
  if not request.user.is_authenticated():
    raise PermissionDenied
  page_number = 1
  try:
    page_number = int(request.GET["p"])
  except:
    pass

  qs = get_user_takeleave_queryset(request.user.id)

  pagination = generate_pagination(request, qs, 30)

  for obj in pagination.page.object_list:
    obj.minutes = round((obj.end_time - obj.start_time).total_seconds() / 60.0, 2)
    obj.status_name = status_to_text(obj.status)

  return TemplateResponse(request, "attendance/takeleave_audit.html",{
    "pagination": pagination,
  })


def takeleave_list(request):
  if not request.user.is_authenticated():
    raise PermissionDenied

  page_number = 1
  try:
    page_number = int(request.GET["p"])
  except:
    pass

  qs = TakeleaveEntry.objects
  qs = qs.filter(user=request.user.id).exclude(status=STATUS_CANCEL)
  qs = qs.order_by("-pub_date")

  pagination = generate_pagination(request, qs, 30)

  for obj in pagination.page.object_list:
    obj.minutes = round((obj.end_time - obj.start_time).total_seconds() / 60.0, 2)
    obj.status_name = status_to_text(obj.status)

  return TemplateResponse(request, "attendance/takeleave_list.html", {
    "pagination": pagination,
  })

def cancel_takeleave(request):
  if request.user.is_authenticated():
    _id = int(request.GET["q"])

    try:
      entry = TakeleaveEntry.objects.get(id=_id)
      if entry.user_id == request.user.id:
        entry.status = STATUS_CANCEL
        entry.save()
        return JsonResponse({
          "message": u"delete!",
          "code": 0,
          })
    except TakeleaveEntry.DoesNotExist:
      pass
  
  return JsonResponse({
    "message": u"failed",
    "code": 1,
    })

def apply_takeleave(request):
  if not request.user.is_authenticated():
    raise PermissionDenied

  if request.method == "POST":
    form = ApplyTakeleaveForm(request.POST)
    if form.is_valid():
      print "->" * 100
      start_time = form.cleaned_data["start_time"]
      end_time = form.cleaned_data["end_time"]
      reason = form.cleaned_data["reason"]


      now = timezone.now()

      delta = end_time - start_time
      print "delta", delta
      entry = TakeleaveEntry(
          user = request.user,
          start_time = start_time,
          end_time = end_time,
          status = STATUS_WAIT,
          reason = reason,
          pub_date = now,
          )
      entry.save()
      
      redirect_to = reverse_url("takeleave_list")
      return HttpResponseRedirect(redirect_to)
  else:
    form = ApplyTakeleaveForm()

  return render(request, 'attendance/apply_takeleave.html', {
    "form": form,
    })
