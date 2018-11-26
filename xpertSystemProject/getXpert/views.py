from django.shortcuts import (
	render, HttpResponseRedirect, HttpResponse, render_to_response, redirect
)

from django.views.generic import (
	TemplateView, CreateView, FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (
	authenticate, login, logout
)
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from django.contrib.auth.decorators import login_required

from .models import User


# Create your views here.


class UserRegistrationView(CreateView):
	template_name = 'signup.html'
	form_class = UserRegistrationForm
	success_url = reverse_lazy('landing_page')

	def form_valid(self, form):
		# print('in form valid')
		new_object = form.save(commit=False)
		# password = form.cleaned_data['password']
		# print(password)
		new_object.password = make_password(form.cleaned_data['password'])
		new_object.is_active = True
		new_object.save()
		# form.save()
		return super(UserRegistrationView, self).form_valid(form)


class UserProfileCreationView(CreateView):
	template_name = 'createProfile.html'



# class LoginView(FormView):
#     success_url = reverse_lazy("thanks_page")
#     form_class= AuthenticationForm
#     redirect_field_name = REDIRECT_FIELD_NAME
#
#     @method_decorator(sensitive_post_parameters('password'))
#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):
#         request.session.set_test_cookie()
#
#         return super(LoginView, self).dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         auth_login(self.request, form.get_user())
#
#         #If the test cookie worked, go ahead and
#         #delete it since it is no longer needed
#         if self.request.session.test_cookie_worked():
#             self.request.session.delete_test_cookie()
#
#
#         return super(LoginView, self).form_valid(form)
#
#     def get_success_url(self):
#         redirect_to = self.request.GET(self.redirect_field_name)
#         if not is_safe_url(url=redirect_to, host=self.request.get_host()):
#             redirect_to = self.success_url
#         return redirect_to
#

def user_login(request):
	context = RequestContext(request)
	context_return={}
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
			# is_active is checked to make sure that the user
			# has not deleted the account.
			# For deletion we don't delete the account we set the is_active to False
			if user.is_active:
				login(request, user)
				print('login sucessfull')
				return redirect('thanks_page')
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


class Thanks(TemplateView):
	template_name = 'thanks.html'

# class LoginView():
