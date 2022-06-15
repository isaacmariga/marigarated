from rest_framework import serializers
from .models import Profile, Projects, Review


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
      model = Profile
      fields = ('picture', 'bio', 'user')

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
      model = Projects
      fields = ('title', 'image', 'description', 'link', 'user')