from django.shortcuts import render
from .models import Profile, Projects

# Create your views here.


def welcome(request):
		return render(request, 'test.html')

def home(request):
	projects = Projects.get_all()

	return render(request, 'awards/home.html', {'projects': projects})

def project(request, title):
	project = Projects.get_by_title(title)
	title = project.title

	return render(request, 'awards/project.html', {'project': project, "title":title})

def profile(request, user):
	profile = Profile.get_by_user(user)

	return render(request, 'awards/profile.html', {'profile': profile, "user":user})

def search_project(request):
	if 'search_project' in request.GET and request.GET['search_project']:
		title = request.GET.get('search_project')
		projects = Projects.filter_by_title(title)
		message = f'{title}'

		return render(request, 'awards/search_project.html', {'message':message, 'projects':projects})
		# if it is a search bar:
	else :
		message = 'We have not found your search term'
		return render(request, 'awards/search_project.html', {'message':message, 'projects':projects})

