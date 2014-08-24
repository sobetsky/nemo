#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
import datetime

class Share(object):
	def __init__(self, name, sector):
		self.__name=name
		self.__sector=sector
		self.__url='http://www.google.com/finance/'

	name=property(lambda self:self.__name) 
	sector=property(lambda self:self.__sector)
	url=property(lambda self:self.__url)


	def ValCur(self):
		html_doc = urlopen('https://www.google.com/finance?q='+self.__name).read()
		soup = BeautifulSoup(html_doc)

		p=soup.find('span','pr')
		p=p.find('span')
		p=float(p.string)
		
		v=soup.find('table', 'snap-data')
		v=v.find_all('td', 'val')
		r=v[3].string
		v_=r.split('/')
		v=v_[0]
		v_=v_[1]
		
		now_=datetime.datetime.now()
		now=now_.strftime('%d %b.%Y %H:%M')
		w=('monday','tuesday','wednsday','thursday','friday','saturday','sunday')
		n=now_.weekday()
		dw=w[n]	

		return now, dw, p, v, v_

			
if __name__=='__main__':
	share=Share('aa', 'bm')
	print share.name
	print share.sector
	print share.url
	print share.ValCur()
	






        
        


    								


        
