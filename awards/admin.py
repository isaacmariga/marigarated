from django.contrib import admin
from .models import Profile, Projects, Review, Text
# Register your models here.


admin.site.register(Projects)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Text)

