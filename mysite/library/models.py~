#!/usr/lib/python 2.7
# -*- coding: utf-8 -*- 
from django.db import models


class Publisher(models.Model):
	name=models.TextField()
	address=models.TextField(blank=True)
	city=models.TextField()
	country=models.TextField()
	website=models.URLField(blank=True)
	def __unicode__(self):
		return self.name

	class Meta:
		ordering=['name']

class Author(models.Model):
	first_name=models.TextField()
	second_name=models.TextField()
	e_mail=models.EmailField(blank=True, verbose_name='e-mail')
	def __unicode__(self):
		return '%s %s'%(self.first_name, self.second_name)

	class Meta:
		ordering=['first_name', 'second_name']

class Book(models.Model):
	title=models.CharField(max_length=50)
	authors=models.ManyToManyField(Author)
	publisher=models.ForeignKey(Publisher)
	publication_date=models.DateField(blank=True, null=True)
	def __unicode__(self):
		return self.title

	class Meta:
		ordering=['title']

























