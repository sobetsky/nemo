#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from library.models import Publisher, Author, Book

class PublisherForm(forms.Form):
	name=forms.CharField(max_length=20)
	address=forms.CharField(required=False, max_length=20)
	city=forms.CharField(max_length=20)
	country=forms.CharField(required=False, max_length=20)
	www =forms.URLField(required=False, label='web-site')
	

'''
	message=forms.CharField(widget=forms.Textarea)
	def clean_message(self):
		message=self.cleaned_data['message']
		num_words=len(message.split())
		if num_words<4:
			raise forms.ValidationError(" мало слов!")
		return message
'''
'''
class BookForm(forms.Form):
	title=forms.CharField(max_length=20)

	def get_my_publisher():
		# you place some logic here
		publishers=Publisher.objects.all()
		#choices_list=(publishers,)
		choices_list=(
			('1', 'Option 1'),
			('2', 'Option 2'),
			('3', 'Option 3'),
		)
		return choices_list
	publisher = forms.ChoiceField(choices=get_my_publisher())
	
	def get_my_author():
		#authors=Author.objects.all()
		#choices_list=(authors,)
		choices_list = (
			('blue', 'Blue'),
           	('green', 'Green'),
           	('black', 'Black')
		)
		return choices_list
	authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())


	publication_date=forms.DateField()
	comment = forms.CharField(widget=forms.TextInput(attrs={'size':'50'}))
#attrs={'cols': 80, 'rows': 20}

'''

class BookForm(ModelForm):
	class Meta:
		model=Book


































