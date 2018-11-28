from django.shortcuts import (
	render, HttpResponseRedirect, HttpResponse, render_to_response, redirect
)
from .utils import identicon_generation
from django.views.generic import (
	TemplateView, CreateView, FormView, DetailView
)
import json
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password

from django.contrib.auth import (
	authenticate, login, logout
)
from django.template import RequestContext
from django.utils.decorators import method_decorator


from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Q
from .models import User, User_profile


# Create your views here.


class UserRegistrationView(CreateView):
	template_name = 'signup.html'
	form_class = UserRegistrationForm
	success_url = reverse_lazy('registration_page')

	def form_valid(self, form):
		# print('in form valid')
		new_object = form.save(commit=False)
		# password = form.cleaned_data['password']
		# print(password)
		new_object.password = make_password(form.cleaned_data['password'])
		new_object.is_active = True
		new_object.save()
		# form.save()
		messages.success(self.request,'Registration Successful')
		return super(UserRegistrationView, self).form_valid(form)


@never_cache
@login_required
def UserProfileCreationView(request):
	#print(request.user.email)
	user_email = request.user.email
	gravatar_url = identicon_generation(user_email)
	context = {'img_url':gravatar_url}
	if request.method =='POST':
		form = UserProfileForm(request.POST)
		if form.is_valid():
			print(request.POST.get('Gender'))
			obj = User_profile()
			obj.user = request.user
			obj.profile_pic = gravatar_url
			obj.gender = form.cleaned_data['gender']
			obj.date_of_birth = form.cleaned_data['date_of_birth']
			permanent_add = form.cleaned_data['permanent_address']
			country = request.POST.get('category')
			state = request.POST.get('activity')
			permanent_add = permanent_add + ", "+state+", "+country
			obj.permanent_address = permanent_add
			obj.qualification = form.cleaned_data['qualification']
			obj.occupation = form.cleaned_data['occupation']
			skills = form.cleaned_data['skills']
			skills_list = skills.split(',')
			skills_obj = json.dumps(skills_list)
			obj.skills = skills_obj
			obj.phone_number = form.cleaned_data['phone_number']
			obj.Available_service_area = form.cleaned_data['Available_service_area']
			obj.languages_spoken = form.cleaned_data['languages_spoken']
			obj.Working_experience = form.cleaned_data['Working_experience']
			obj.charges = form.cleaned_data['charges']
			obj.Profile_Tagline = form.cleaned_data['Profile_Tagline']
			obj.save()
			return HttpResponseRedirect(reverse_lazy('thanks_page'))

		else:
			print('invalidForm')
			context = {'form':form}
			return render(request, 'createProfile.html', context)
			#return HttpResponseRedirect(reverse_lazy('createProfile'))

	return render(request, 'createProfile.html',context)

def user_login(request):
	context = RequestContext(request)
	context_return={}
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email.lower(), password=password)
		if user is not None:
			# is_active is checked to make sure that the user
			# has not deleted the account.
			# For deletion we don't delete the account we set the is_active to False
			if user.is_active:
				login(request, user)
				print('login sucessfull')
				db_user = User_profile.objects.filter(user=request.user)
				if db_user:
					return redirect('thanks_page')
				else:
					return redirect('createProfile')
			else:
				return HttpResponse("is_active not working")
		else:
			error='Invalid login details'
			context_return['error']=error
			return render(request,'Login.html',context_return)

	else:
		return render(request, 'Login.html', {})


@login_required
def user_logout(request):
	context = RequestContext(request)
	logout(request)
	return redirect('login')


# @method_decorator(login_forbidden, name='dispatch')
class LandingPageView(TemplateView):
	template_name = 'index.html'
	def dispatch(self, request, *args, **kwargs):
		if self.request.user.id is None:
			return super(LandingPageView, self).dispatch(request, *args, **kwargs)
		else:
			return redirect('thanks_page')



class Thanks(TemplateView):
	template_name = 'view_profile.html'

# class LoginView():

@login_required
def search_user(request):
	if request.method == 'POST' and request.POST['searchSkills'] and request.POST['searchLocation']:
		searchSkills = str(request.POST['searchSkills']).strip()
		searchLocation = str(request.POST['searchLocation']).strip()
		print(searchSkills)
		searchLocationList = list(
			User_profile.objects.order_by().values_list('Available_service_area', flat=True).distinct())
		user_profile_object = User_profile.objects.filter(Q(skills__icontains=searchSkills) & Q(
			Available_service_area__icontains=searchLocation))  # icontains is for case insensitive search
		return render(request, 'ajax_search.html',
		              {'user_profile_object': user_profile_object, 'searchLocationList': searchLocationList})
	else:
		searchLocationList = list(
			User_profile.objects.order_by().values_list('Available_service_area', flat=True).distinct())
		print(searchLocationList)
		return render(request, 'search.html', {'searchLocationList': searchLocationList})
