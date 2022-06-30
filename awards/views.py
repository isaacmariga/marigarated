from django.shortcuts import redirect, render
from .models import Profile, Projects, Review
from .forms import ProfileForm, ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectsSerializer

# Create your views here.


def home(request):
		projects = Projects.get_all()
		project = Projects.get_all().first()

		title = 'Home'

		return render(request, 'awards/home.html', {'projects': projects,  'title': title, 'project': project})


def project(request, id):
		project = Projects.get_by_id(id)
		# project = Projects.get_by_id(id)
		title = project.title

		return render(request, 'awards/project.html', {'project': project, "id": id, 'project': project, 'title': title})


@login_required(login_url='/accounts/login/')
def profile(request, user):
		profile = Profile.get_by_user(user)
		projects = Projects.filter_by_user(user)
		# title = profile.user

		return render(request, 'awards/profile.html', {'profile': profile, "user": user, 'projects': projects})


def search_project(request):
		if 'search_project' in request.GET and request.GET['search_project']:
				print(request.GET['search_project'])
				title = request.GET.get('search_project')
				projects = Projects.filter_by_title(title)
				message = f'{title}'

				return render(request, 'awards/search_project.html', {'message': message, 'projects': projects})
				# if it is a search bar:
		else:
				message = 'We have not found your search term'
				return render(request, 'awards/search_project.html', {'message': message, 'projects': projects})


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
				form = ProjectForm()

		return render(request, 'awards/new_project.html', {'form': form, })


@login_required(login_url='/accounts/login/')
def edit_profile(request):
		current_user = request.user

		if request.method == 'POST':
				form = ProfileForm(request.POST, request.FILES)

				if form.is_valid():
						profile = form.save(commit=False)
						profile.user = current_user
						profile.save()
				return redirect('profile', current_user)
		else:
				form = ProfileForm()

		return render(request, 'django_registration/registration_complete.html', {'form': form})


@login_required(login_url='/accounts/login/')
def review(request, id):
		current_user = request.user
		project = Projects.get_by_id(id)
		d_avg = Review.design_avg(id)
		c_avg = Review.content_avg(id)
		u_avg = Review.user_avg(id)

		if request.method == 'POST':

				form = ReviewForm(request.POST)
				if form.is_valid():
						review = form.save(commit=False)
						review.user = current_user
						review.project = project
						profiles = current_user.profile_set.values()

						for profile in profiles:
								review.profile_id = profile['id']
								form.save()
				return redirect('review', project.id)
		else:

				form = ReviewForm()

		return render(request, 'awards/review.html', {'form': form, 'id': id, 'project': project, 'd_avg': d_avg, 'c_avg': c_avg, 'u_avg': u_avg})


class ProjectList(APIView):
		def get(self, request, format=None):
				projects = Projects.get_all()
				serializers = ProjectsSerializer(projects, many=True)
				return Response(serializers.data)


class ProfileList(APIView):
		def get(self, request):
				profile = Profile.get_all_profiles()
				print("test--"+str(profile))

				serializers = ProfileSerializer(profile, many=True)
				return Response(serializers.data)

class DesignAvg(APIView):
		def get(self, request, id):
				# projects = Projects.get_all()
				design_avg = Review.design_avg(id)
				print("test--"+str(design_avg))
				return Response({"averages":int(design_avg)})
