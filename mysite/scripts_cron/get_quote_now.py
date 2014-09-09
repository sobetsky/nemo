#!/usr/bin/python2.7
# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen

s='aa'
html_doc = urlopen('https://www.google.com/finance?q='+s).read()
soup = BeautifulSoup(html_doc)
p=soup.find('span','pr')
p=p.find('span')
#i=t.get('id')
p=p.string

v=soup.find('table', 'snap-data')
v=v.find_all('td', 'val')
r=v[3].string
v_=r.split('/')
v=v_[0]
v_=v_[1]

print p,v,v_

