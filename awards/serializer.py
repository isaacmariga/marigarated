from rest_framework import serializers
from .models import Profile, Projects, Review, Text


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
      model = Profile
      fields = ('picture', 'bio', 'user')
class TextSerializer(serializers.ModelSerializer):
    class Meta:
      model = Text
      fields = ('text',)


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
      model = Projects
      fields = ('title', 'image', 'description', 'link', 'user')
      depth = 1
