#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen

class EconomicCalendar(object):

	def __init__(self):
		self.__url='http://finviz.com/calendar.ashx'

	url=property(lambda self:self.__url) 


	def CalWeek(self):
		html_doc = urlopen(self.__url).read()
		soup     = BeautifulSoup(html_doc) 
		cal      = soup.find_all('td','calendar')
		cal=str(cal)
		cal=cal[1:-1]
		#c=cal.count('gfx/calendar/impact_3.gif')
		#print c
		cal=cal.replace('gfx/calendar/impact_1.gif','../static/gfx/calendar/impact_1.gif')
		cal=cal.replace('gfx/calendar/impact_2.gif','../static/gfx/calendar/impact_2.gif')
		cal=cal.replace('gfx/calendar/impact_3.gif','../static/gfx/calendar/impact_3.gif')
		cal='<table width=720px>'+cal+'</table>'
		with open("/srv/vhosts/mysite/templates/calendar/_calendar.html", "wt") as code:
			code.write(cal)

		week     = soup.find_all('table','calendar')
 		#l=len(week) 
		#day=week[l-1]
		for day in week:
			day=day.find_all('tr')
			day_0=day[0].find_all('td')
			day_data=day_0[0].get_text()
			print (day_data)

			for hour in day[1:]:
				hour=hour.find_all('td')

				day_hour=hour[0].get_text()
				day_hour_Release=hour[2].get_text()
				if day_hour_Release in 'No economic releases':
					print day_hour_Release
					continue
				day_hour_Release_Impact_for=hour[4].get_text()	
				day_hour_Release_Impact_for_acl=hour[5].get_text()	
				day_hour_Release_Impact_for_exp=hour[6].get_text()	
				day_hour_Release_Impact_for_pri=hour[7].get_text()

				Impact=hour[3].find('img')
				day_hour_Release_Impact=Impact.get('src')
				if 'gfx/calendar/impact_3.gif' in str(day_hour_Release_Impact):
					

					print (day_hour, day_hour_Release, day_hour_Release_Impact)

			print 'xxxxxxxxxxx'

		st=str(day_hour)
		return st

if __name__=='__main__':

	p=EconomicCalendar()
	print p.url
	p.CalWeek()


