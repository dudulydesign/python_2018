from django import forms

def ApplyOvertimeForm(*args, **kwargs):
  from .models import Department
  department = list(Department.objects.order_by("-ordering"))
  choices = [(d.id, d.name) for d in department]


  class ApplyOvertimeForm(forms.Form):
    department = forms.ChoiceField(choices=choices)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    reason = forms.CharField(widget= forms.Textarea)

  return ApplyOvertimeForm

class OvertimeAuditForm(forms.Form):

  status = forms.ChoiceField(choices=[(1, 'OK'), (0, 'NO')])
  #reason = forms.CharField()

