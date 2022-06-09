from django import forms
from .models import Profile, Projects


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Projects
    exclude = ['user']
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']