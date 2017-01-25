from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login_view, name='login'),
	url(r'^signup/$', views.signup_view, name='signup'),
	url(r'^profile/$', views.myprofile_view, name='myprofile_view'),
]
