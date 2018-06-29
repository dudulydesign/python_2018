from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import LoginForm
from attendance.views import leader_audit_list
from attendance.queries import get_user_overtime_queryset
from takeleave.views import takeleave_audit_list
from takeleave.queries import get_user_takeleave_queryset


def index(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect(reverse_url("login"))


  overtime_qs = get_user_overtime_queryset(request.user.id)

  #select count(*) from table where .......
  overtime_count = overtime_qs.count()


  return TemplateResponse(request, "index.html", {
    "overtime_count":overtime_count
  })

def login_view(request):
  print "=>" * 100
  print "login_view"
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      print "is_valid!!!"
      user = form.user
      auth_login(request, user)
      url2 = reverse_url("index")
      return HttpResponseRedirect(url2)
  else:
    form = LoginForm()
  return TemplateResponse(request, "login.html", {
    "login_form": form,
    })

def logout_view(request):
  auth_logout(request)
  url2 = reverse_url("index")
  return HttpResponseRedirect(url2)
