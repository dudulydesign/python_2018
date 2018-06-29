from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import LoginForm
from attendance.views import leader_audit_list

def index(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect(reverse_url("login"))

  audit_wait = 10
  '''
  audit_wait = leader_audit_list.objects
  audit_wait = audit_wait.count(status=STATUS_WAIT)
  try:
    overtime_count = int(request.GET["p"])
  except:
    pass

  audit_view = list(leader_audit_list.objects.count(status_id=request.status).all())
  audit_count = [s.audit_count for s in audit_view]
  print "audit_count", audit_count


'''
  return TemplateResponse(request, "index.html", {
    "audit_wait":audit_wait
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
