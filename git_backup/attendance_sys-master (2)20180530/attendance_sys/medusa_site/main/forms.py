from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
  username = forms.CharField(min_length=3)
  password = forms.CharField(widget=forms.PasswordInput)

  def clean(self):
    cleaned_data = self.cleaned_data
    print "cleaned_data", cleaned_data
    username = cleaned_data["username"]
    password = cleaned_data["password"]
    try:
      user = User.objects.get(username=username)
    except User.DoesNotExist:
      raise forms.ValidationError(u"使用者不存在!")

    print "check_password", user.check_password(password)
    if user.check_password(password) == False:
      raise forms.ValidationError(u"密碼錯誤!")

    self.user = user
    cleaned_data["user"] = user

    return cleaned_data
