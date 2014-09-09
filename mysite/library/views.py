#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
#  /shares/views.py

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



from library.models import Publisher, Author, Book
from library.forms import PublisherForm
from library.forms import BookForm


###  /library/  ##################################################################################

def library_(request):
	str_="<img src='/static/img/books.jpg' width='50' height='50'/> "
	str_+="<a href='/'>home</a>"
	str_+="&nbsp&nbsp&nbsp"
	str_+="<a href='/library/search/'>search_form</a>"
	str_+="&nbsp&nbsp&nbsp"
	str_+="<a href='/library/enter/'>Enter_form</a>"
	str_+="&nbsp&nbsp&nbsp"
	str_+="<a href='/admin/'>admin</a>"
	return HttpResponse(str_) 
###  /library/search  ############################################################################
@csrf_exempt

def search_(request):

	errors_title=[]
	if 'q_title' in request.POST:
		q_title=request.POST['q_title']
		if not q_title:
			errors_title.append('Введите запрос.')
		elif len(q_title)>20:
			errors_title.append('Введено более 20 символов.')
		else:
			books=Book.objects.filter(title__icontains=q_title)
			return render_to_response('library/_search_form.html', locals())

	errors_author=[]
	if 'q_author' in request.POST:
		q_author=request.POST['q_author']
		if not q_author:
			errors_author.append('Введите запрос.')
		elif len(q_author)>20:
			errors_author.append('Введено более 20 символов.')
		else:
			authors=Author.objects.filter(second_name__icontains=q_author)
			
			return render_to_response('library/_search_form.html', locals())

	errors_publisher=[]
	if 'q_publisher' in request.POST:
		q_publisher=request.POST['q_publisher']
		if not q_publisher:
			errors_publisher.append('Введите запрос.')
		elif len(q_publisher)>20:
			errors_publisher.append('Введено более 20 символов.')
		else:
			publishers=Publisher.objects.filter(name__icontains=q_publisher)
			#return render_to_response('library/_search_form.html', locals())

	return render_to_response('library/_search_form.html', locals())


###  /library/enter  ############################################################################
@csrf_exempt

def enter_(request):
	form_publisher=PublisherForm()
	form_book=BookForm()
	#publishers=Publisher.objects.all()
	#authors=Author.objects.all()	
	

	if 'author_form' in request.POST:
		errors_first_name=[]
		errors_second_name=[]
		st=''
		if 'first_name' in request.POST:
			first_name=request.POST['first_name']
			if not first_name:
				errors_first_name.append('Введите имя.')
			elif len(first_name)>20:
				errors_first_name.append('Введено более 20 символов.')
			else:
				#publishers=Publisher.objects.filter(name__icontains=q_publisher)	
				pass
		if 'second_name' in request.POST:
			second_name=request.POST['second_name']
			if not second_name:
				errors_second_name.append('Введите фамилию.')
			elif len(second_name)>20:
				errors_second_name.append('Введено более 20 символов.')
			else:
				#publishers=Publisher.objects.filter(name__icontains=q_publisher)	
				pass
		if first_name and second_name:
			e_mail=request.POST['e_mail']
			#st=first_name+' '+second_name+' '+e_mail
			Author.objects.create(first_name=first_name, second_name=second_name, e_mail=e_mail)
		return render_to_response('library/_enter_form.html', locals())


	if 'publisher_form' in request.POST:
		form_publisher=PublisherForm(request.POST)
		if form_publisher.is_valid():
			cd=form_publisher.cleaned_data
			q1=Publisher.objects.create(name=cd['name'], address=cd['address'], city=cd['city'], country=cd['country'], website=cd['www']) 
			#return render_to_response('library/_enter_form.html', locals())



	if 'book_form' in request.POST:
		form_book=BookForm(request.POST)

		if form_book.is_valid():
			#author = form.save(commit=False)
			#author.title = 'Mr'
			#author.save()
			form_book.save()
			#cd=form_book.cleaned_data
			#title=cd['title']
			#publisher=cd['publisher']
			#authors=cd['authors']



	return render_to_response('library/_enter_form.html', locals())


###  /library/lab  ############################################################################
@csrf_exempt
def lab(request):
	#st="<img src='../../static/img/bl.jpg' width='50' height='50'/>"
	#Publisher.objects.filter(name='Самиздат').delete()
	#Publisher.objects.all().delete()
	#Author.objects.all().delete()
	#Book.objects.all().delete()
	#Book.objects.filter(title='Рожденный ползать, летать не может.').delete()

	form_book=BookForm(request.POST)
	authors=request.POST.get('authors')
	#cd=form_book.cleaned_data
	
	return render_to_response('library/lab.html', locals())

























