from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.login_view, name='login'),
	url(r'^register/$', views.signup_view, name='signup'),
	url(r'^profile/$', views.myprofile_view, name='myprofile_view'),
	url(r'^logout/$', views.logout_view , name='logout_view'),
	url(r'^theme1/$', views.themeoneview , name='theme_one_view'),
	url(r'^theme2/$', views.themetwoview , name='theme_two_view'),
	url(r'^link/$', views.link_generate , name='link_generate_view'),
]
