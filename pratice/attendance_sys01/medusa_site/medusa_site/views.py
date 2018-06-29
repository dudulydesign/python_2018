from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from main.forms import LoginForm

def index(request):
  print "user", request.user, request.user.id, request.user.is_authenticated
  login_form = LoginForm()

  return TemplateResponse(request, "index.html", {
    "login_form": login_form,
    })
  
@csrf_project
def login(request):
  return render_to_response('index.html', context_instance=RequestContext(request))
