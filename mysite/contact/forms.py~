#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

from django import forms

class ContactForm(forms.Form):
	subject=forms.CharField(max_length=100)
	e_mail =forms.EmailField(required=False, label='Your e-mail')
	message=forms.CharField(widget=forms.Textarea)

	def clean_message(self):
		message=self.cleaned_data['message']

		num_words=len(message.split())
		if num_words<4:
			raise forms.ValidationError(" мало слов!")
		return message

