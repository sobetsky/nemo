#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import views


import shares.views
import shares.urls
import library.views
import library.urls
import contact.views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^$',views.page_0),
	(r'^accounts/login/$',login),
	(r'^accounts/profile/$',views.profile_),
	(r'^accounts/logout/$',logout),
	(r'^home/$',views.page_home),
	(r'^calendar/$',views.page_calendar),
	(r'^contact/$',contact.views.contact_),
	(r'^shares/$',shares.views.shares_),
	(r'^shares/',include(shares.urls)),

	(r'^library/',include(library.urls)),
	#(r'^library/$',library.views.library_),
	)



























