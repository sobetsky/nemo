#!/usr/bin/python2.7
# -*- coding: utf8 -*-
# В crontab прописать исполнение, раз в неделю, в понедельник, в 15:00
from bs4 import BeautifulSoup
from urllib2 import urlopen
#Получить страницу 
html_doc = urlopen('http://finviz.com/calendar.ashx').read()
soup = BeautifulSoup(html_doc)
#print soup

# Содержимое мета полей
#for meta in soup.find_all('meta'):
#    print(meta.get('content'))

#Поиск по ссылкам
#for link in soup.find_all('a'):
#    print link.get('href')
# Содержимое ссылок
#for link in soup.find_all('a'):
#    print link.contents[0]

# Содержимое из <div class="content"> ... </div>
#print soup.find('div', 'content')
 
# Блок: <div id="top_menu"> ... </div>
#print soup.find('div', id='top_menu')

#t=soup.find_all('tr')

data=soup.find_all('td','calendar')

print t


#-----------------------------------------------------------
#data=soup.find_all('td','calendar')
#data=str(data)
#data=data[1:-1]
#data='<table width=720px>'+data+'</table>'

#with open("/srv/vhosts/mysite/templates/calendar/_calendar.html", "wt") as code:
#	code.write(data)

