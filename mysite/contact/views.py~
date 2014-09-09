#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
import datetime
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import random 
from contact.forms import ContactForm
from django.core.mail import send_mail

@csrf_exempt

def contact_(request):

	#form_cont=ContactForm()
	form_cont=ContactForm(initial={ 'subject':' subject', 'e_mail':''})

	if request.method=='POST':
		form_cont=ContactForm(request.POST)
		if form_cont.is_valid():
			cd=form_cont.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('e_mail', 'noreply@example.com'),
				['i.sobetskyi@gmail.com' ],
			)
			message_sand='message was sand'
			#return HttpResponseRedirect('/contact')

	
	return render_to_response('contact/_contact_form.html', locals()) 































