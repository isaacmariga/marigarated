from rest_framework import serializers
from .models import Profile, Projects, Review, Text, Test1, Test2, Test3


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


class Test1Serializer(serializers.ModelSerializer):
    class Meta:
      model = Test1
      fields = ('test1',)

class Test2Serializer(serializers.ModelSerializer):
    class Meta:
      model = Test2
      fields = ('test2',)
class Test3Serializer(serializers.ModelSerializer):
    class Meta:
      model = Test1
      fields = ('test1', 'test2')

