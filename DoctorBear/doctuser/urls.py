from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index2, name='index2'),
	url(r'^login/xxid=(?P<xxid>[\w]*)/$',views.login,name='login'),
	url(r'^handle/',views.handle,name='handle'),
	# url(r'^mypost/',views.mypost,name='mypost'),
	
]