from django import forms


def ApplyTakeleaveForm(*args, **kwargs):

  from .models import Category
  from .models import Department
  categories = list(Category.objects.order_by("-ordering"))
  choices = [(c.id, c.name) for c in categories]

  department = list(Department.objects.order_by("-ordering"))
  choices2 = [(d.id, d.name) for d in department]


  class ApplyTakeleaveForm(forms.Form):
    category = forms.ChoiceField(choices=choices)
    #category = forms.ChoiceField(choices=[(0, ''),(1, 'Leave for Statutory Reasons'),(2, 'Personal Leave'),(3, 'Menstrual Leave'),(4, 'Sick Leave')])
    department = forms.ChoiceField(choices=choices2)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    reason = forms.CharField(widget = forms.Textarea)

  return ApplyTakeleaveForm



class TakeleaveAuditForm(forms.Form):
  status = forms.ChoiceField(choices=[(1, 'OK'),(0, 'NO')])
