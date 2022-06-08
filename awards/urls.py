from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
  path('', views.home,name ='home'),
  path('project/<title>', views.project,name = 'project'),
  path('profile/<user>', views.profile,name = 'profile'),
  path('search_project/', views.search_project,name = 'search_project'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
