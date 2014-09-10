#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
import datetime
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import random 

  
###  home_0  ################################################################

#@login_required
def page_0(request):
	'''
	str_="<ul><a href='home/'><b>mysite.com/home</b></a></ul>"
	str_+="<hr>"
	str_+="<ul><a href='contact/'><b>mysite.com/contact</b></a></ul>"
	str_+="<hr>"
	str_+="<ul><a href='shares/'><b>mysite.com/shares</b></a>"
	str_+="<li>1</li>"
	str_+="<li>2</li></ul>"
	str_+="<hr>"
	str_+="<ul><a href='library/'><b>mysie.com/library</b></a>"
	str_+="<li><a href='library/enter/'>mysie.com/library/enter</a></li>"
	str_+="<li><a href='library/search/'>mysie.com/library/search</a></li></ul>"
	#str_+="<li><a href='library/lab/'>mysie.com/library/lab</a></li></ul>"
	#str_+="<hr>"
	str_+="<ul><a href='admin/'><b>mysie.com/admin/library</b></a></ul>"
	#str_+="<li>1</li>"
	#str_+="<li>2</li></ul>"
	str_+="<hr>"
	return HttpResponse(str_) 
	'''
	#return render_to_response('home.html')
	return HttpResponseRedirect('home/')

###  profile   ###############################################################
def profile_(request):
	
	return HttpResponseRedirect('home/')

###  /home  ##################################################################

def page_home(request):
	now, dw=now_weeck()
	s1,s2,s3=rendom_word()


	return render_to_response('home.html', locals())

###  /calendar  ##############################################################

def page_calendar(request):
	now, dw=now_weeck()
	s1,s2,s3=rendom_word()

	return render_to_response('calendar/calendar.html', locals())


### FUNCTIONS ################################################################
def now_weeck():
	now_=datetime.datetime.now()
	now=now_.strftime('%d %b.%Y')
	w=('monday','tuesday','wednsday','thursday','friday','saturday','sunday')
	n=now_.weekday()
	dw=w[n]
	return(now, dw)

#-----------------------------------------------------------------------------

def rendom_word():

	s1=['я','глубоко','выдохнул','и','стал','наблюдать']
	s2=['сначала','наблюдал','за','собой',',','потом','за','будущем']
	s3=['я','стал','величайшим','наблюдателем']

	r=random.randint(1,3)
	if r==1:
		n=random.randint(1,5)
		w=s1.pop(n)
		#w="<span style='color:green;'>"+w+'</span>'
		n=random.randint(0,4)
		s1.insert(n,w)
		s1=' '.join(s1)+'.'
		s2=' '.join(s2)+'.'
		s3=' '.join(s3)+'.'
	elif r==2:
		n=random.randint(0,6)
		w=s2.pop(n)
		#w="<span style='color:green;'>"+w+'</span>'
		n=random.randint(0,5)
		s2.insert(n,w)
		s1=' '.join(s1)+'.'
		s2=' '.join(s2)+'.'
		s3=' '.join(s3)+'.'
	elif r==3:
		n=random.randint(1,3)
		w=s3.pop(n)
		#w="<span style='color:green;'>"+w+'</span>'
		n=random.randint(0,2)
		s3.insert(n,w)
		s1=' '.join(s1)+'.'
		s2=' '.join(s2)+'.'
		s3=' '.join(s3)+'.'

	# Декодируем из utf8 в unicode - из внешней в рабочую
	s1 = s1.decode('utf8')
	s2 = s2.decode('utf8')
	s3 = s3.decode('utf8')

	s1=s1.capitalize()
	s2=s2.capitalize()
	s3=s3.capitalize()

	# Кодируем тест из unicode в utf8 - из рабочей во внешнюю
	#text = text.encode('utf8')
	#s1 = s1.encode('utf8')
	#s2 = s2.encode('utf8')
	#s3 = s3.encode('utf8')

	return(s1,s2,s3)























