from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', login_required(LandingPageView.as_view()), name='landing_page'),
    url(r'^registration/', UserRegistrationView.as_view(), name='registration_page'),
    url(r'^login/', user_login, name='login'),
    url(r'^logout/', user_logout, name='logout'),
    url(r'^thanks/', Thanks.as_view(), name='thanks_page'),


]