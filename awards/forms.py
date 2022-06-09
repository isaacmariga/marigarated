from django import forms
from .models import Profile, Projects


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Projects
    exclude = ['user']