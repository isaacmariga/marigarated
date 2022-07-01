from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
  path('', views.home,name ='home'),
  path('project/<id>', views.project,name = 'project'),
  path('profile/<user>', views.profile,name = 'profile'),
  path('search_project/', views.search_project,name = 'search_project'),
  path('new/project/', views.new_project,name = 'new_project'),
  path('review/<id>', views.review,name = 'review'),
  path('accounts/register/complete/', views.edit_profile,name = 'edit_profile'),
  path('api/project/', views.ProjectList.as_view()),
  path('api/profile/', views.ProfileList.as_view()),
  path('api/text/', views.TextList.as_view()),
  path('api/design/<id>', views.DesignAvg.as_view())


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
