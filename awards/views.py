from django.shortcuts import redirect, render
from .models import Profile, Projects, Review

# Create your views here.


def welcome(request):
		return render(request, 'test.html')

def home(request):
	projects = Projects.get_all()

	return render(request, 'awards/home.html', {'projects': projects})

def project(request, id):
	# project = Projects.get_by_title(title)
	project = Projects.get_by_id(id)
	title = project.title

	return render(request, 'awards/project.html', {'project': project, "id":id, 'project':project})

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

def Review_rate(request):
	if request.method == 'GET':
		proj_id = request.GET.get('proj_id')
		project = Projects.objects.get(id=proj_id)
		comment = request.GET.get('comment')
		rate = request.GET.get('rate')
		user = request.user
		Review(user=user, project=project, comment=comment, rate=rate)
		return redirect('project', id=proj_id)