from django.shortcuts import redirect, render
from .models import Profile, Projects, Review
from .forms import ProfileForm, ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def welcome(request):
		return render(request, 'test.html')

def home(request):
	projects = Projects.get_all()
	d_avg = Review.design_avg()
	c_avg = Review.content_avg()
	u_avg = Review.user_avg()

	title = 'Home'
	


	return render(request, 'awards/home.html', {'projects': projects, 'd_avg':d_avg,'c_avg':c_avg, 'u_avg':u_avg, 'title':title})

def project(request, id):
	project = Projects.get_by_id(id)
	# project = Projects.get_by_id(id)
	title = project.title

	return render(request, 'awards/project.html', {'project': project, "id":id, 'project':project, 'title':title})

def profile(request, user):
	profile = Profile.get_by_user(user)
	title = profile.user

	return render(request, 'awards/profile.html', {'profile': profile, "user":user, 'title': title})

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


# @login_required(login_url='/accounts/login/')
# def project_form(request):
# 	current_user = request.user		
# 	if request.method == 'POST':
# 		form = ProjectForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			name = form.save(commit=False)
# 			name.user = current_user
# 			name.save()
# 		return redirect('home')
# 	else:
# 		form = ProjectForm()
			
# 	return render(request, 'awards/new_project.html', {'form': form})



@login_required(login_url='/accounts/login/')
def new_project(request):
	current_user = request.user
	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			upload = form.save(commit=False)
			upload.user = current_user
			upload.save()
		return redirect('home')
	else:
		form=ProjectForm()

	return render(request, 'awards/new_project.html', {'form': form})

@login_required(login_url='/accounts/login/')
def review(request, id):
	current_user = request.user
	project = Projects.get_by_id(id)
	if request.method == 'POST':
		form = ReviewForm(request.POST, request.FILES)
		if form.is_valid():
			upload = form.save(commit=False)
			upload.user = current_user
			upload.project = project
			upload.save()
		return redirect('home')
	else:
		form=ReviewForm()

	return render(request, 'awards/review.html', {'form': form, 'id':id,'project':project})
