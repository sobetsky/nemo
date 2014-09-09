#!/usr/bin/python2.7
# -*- coding: utf8 -*-

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
#shares=bm+ig+cg+th+fn
#shares=list(shares)
path='/srv/vhosts/mysite/data/csv/'

#print shares

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
















