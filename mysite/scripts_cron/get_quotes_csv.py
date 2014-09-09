#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import datetime
#import time
import urllib2
from urllib2 import urlopen
import csv
import psycopg2




def connect_mydb(table_name):
	DSN = 'host=localhost dbname=mydb user=sid password=11111'
	with psycopg2.connect(DSN) as connection:
		with connection.cursor() as cursor:
			cursor.execute('SELECT MAX(id) FROM '+table_name+';')
			id_=cursor.fetchall()
			id_=id_[0][0]
			sql='SELECT s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12 FROM '+table_name+' WHERE id='+str(id_)+';'
			cursor.execute(sql)
			numrows=cursor.fetchall()
			n=int(cursor.rowcount)
	return numrows,n

#####
def get_historical_prices(shares,start,end,path):
	i=0
	while i <len(shares):
		st="https://www.google.com/finance/historical?q="+shares[i]+"&startdate="+start+"&enddate="+end+"&output=csv"
		f = urllib2.urlopen(st)
		print st
		data = f.read()
		with open(path+shares[i]+"_.csv", "wb") as code:
			code.write(data)
		i+=1 
#####
def revers_csv(shares,path):
	j=0
	while j<len(shares):
		f=open(path+shares[j]+"_.csv","rb")
		l_inv=f.readline()
		l=f.readlines()
		f.close
		i=1
		f=open(path+shares[j]+"_.csv","wb")
		for i in l[::-1]:
			l_inv+=i
		f.write(l_inv)
		f.close
		j+=1
#####
def inspection_holes(shares,path):
	j=0
	while j <len(shares):
		str_read=path+shares[j]+"_.csv"
		with open(str_read,"rb") as f:
			reading_f = list(csv.reader(f))

		l_sum=[]
		k=0
		for i in reading_f:

			try:
				float(i[1])
			except ValueError:
				i[1]='0.00'	
			try:
				float(i[2])
			except ValueError:
				i[2]='0.00'	
			try:
				float(i[3])
			except ValueError:
				i[3]='0.00'	
			try:
				float(i[4])
			except ValueError:
				i[4]='0.00'	
			try:
				int(i[5])
			except ValueError:
				i[5]='0'	

			l=[i[0],i[1],i[2],i[3],i[4],i[5]]
			l_sum.append(l)
			k+=1

		l_sum[0]=['\xef\xbb\xbfDate', 'Open', 'High', 'Low', 'Close', 'Volume']

		f=open(str_read,"wb")
		writer=csv.writer(f, dialect='excel')
		for row in l_sum:
			writer.writerow(row)
		f.close
		j+=1
#####
def filling_0(shares,path):
	s=0
	while s <len(shares):
		str_read=path+shares[s]+"_.csv"
		str_writ=path+shares[s]+".csv"

		with open(str_read,"rb") as f:
			reading_f = list(csv.reader(f))

		print shares[s]
		# проверка, если начинается с 0.00
		while reading_f[1][1]=='0.00' or reading_f[1][2]=='0.00' or reading_f[1][3]=='0.00' or reading_f[1][4]=='0.00' or reading_f[1][5]=='0':
			reading_f.pop(1)
		l=range(5)
		for n in l[1:]:
			print n
			start=[]
			end=[]
			k=0
			for i in reading_f:
				if i[n]=='0.00' and reading_f[k-1][n]!='0.00':
					start.append([k, reading_f[k-1][n]])
		
				if i[n]!='0.00' and reading_f[k-1][n]=='0.00':
					end.append([k, i[n]])
				k+=1

			k=0
			for i in start:
				print start[k][0], end[k][0],' | ',start[k][1], end[k][1],' | ', eval('end[k][0]-start[k][0]+1'),' | ', (float(end[k][1])-float(start[k][1]))/eval('end[k][0]-start[k][0]+1')
				k+=1

			for i in range(len(start)):
				d=(float(end[i][1])-float(start[i][1]))/eval('end[i][0]-start[i][0]+1')
				for j in range((eval('end[i][0]-start[i][0]'))):
					print start[i][0]+j, round(float(start[i][1])+(j+1)*d, 2)
					reading_f[start[i][0]+j][n]=round(float(start[i][1])+(j+1)*d, 2)


		start=[]
		end=[]
		k=0
		for i in reading_f:
			if i[5]=='0' and reading_f[k-1][5]!='0':
				start.append([k, reading_f[k-1][5]])
	
			if i[5]!='0' and reading_f[k-1][5]=='0':
				end.append([k, i[5]])
			k+=1
		k=0
		for i in start:
			print start[k][0], end[k][0],' | ',start[k][1], end[k][1],' | ', eval('end[k][0]-start[k][0]+1'),' | ', (int(end[k][1])-int(start[k][1]))/eval('end[k][0]-start[k][0]+1')
			k+=1
		for i in range(len(start)):
			d=(int(end[i][1])-int(start[i][1]))/eval('end[i][0]-start[i][0]+1')
			for j in range((eval('end[i][0]-start[i][0]'))):
				print start[i][0]+j, int(start[i][1])+(j+1)*d
				reading_f[start[i][0]+j][5]=int(start[i][1])+(j+1)*d

		f=open(str_writ,"wb")
		writer=csv.writer(f, dialect='excel')
		for row in reading_f:
			writer.writerow(row)
		f.close
		# Удалить файл _.csv
		s+=1

#####
def lists_shares_csv(bm,ig,cg,th,fn,path):
	with open(path+"bm_list.csv", "wb") as f:
		for share in bm:
			f.write(share+'\n')
	with open(path+"ig_list.csv", "wb") as f:
		for share in ig:
			f.write(share+'\n')
	with open(path+"cg_list.csv", "wb") as f:
		for share in cg:
			f.write(share+'\n')
	with open(path+"th_list.csv", "wb") as f:
		for share in th:
			f.write(share+'\n')
	with open(path+"fn_list.csv", "wb") as f:
		for share in fn:
			f.write(share+'\n')
	shares=bm+ig+cg+th+fn
	with open(path+"shares_list.csv", "wb") as f:
		for share in shares:
			f.write(share+'\n')

######################################################################################################

bm,n=connect_mydb('shares_bm_list')
ig,n=connect_mydb('shares_ig_list')
cg,n=connect_mydb('shares_cg_list')
th,n=connect_mydb('shares_th_list')
fn,n=connect_mydb('shares_fn_list')

bm=list(bm[0])
ig=list(ig[0])
cg=list(cg[0])
th=list(th[0])
fn=list(fn[0])
shares=bm+ig+cg+th+fn

path='/srv/vhosts/mysite/data/csv/'


dt=datetime.datetime.now()
start='Jan+3%2C+2000'
end_=dt.strftime("%b+%d+%Y")
end=end_[:6]+"%2c"+end_[6:]


get_historical_prices(shares,start,end,path)
revers_csv(shares,path)
inspection_holes(shares,path)
filling_0(shares,path)
lists_shares_csv(bm,ig,cg,th,fn,path)





















