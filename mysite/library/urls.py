from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
	(r'enter/$',views.enter_),
	(r'search/$',views.search_),
	(r'lab/$',views.lab),
	(r'$', views.library_),
	)

 
