#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
#  /shares/views.py

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import subprocess



###  /shares  ############################################################################
@csrf_exempt
@login_required
def shares_(request):

	now_=datetime.datetime.now()
	now=now_.strftime('%d %b.%Y : %H.%M')
	w=('monday','tuesday','wednsday','thursday','friday','saturday','sunday')
	n=now_.weekday()
	dw=w[n]

	bm=range(12)
	cg=range(12)
	ig=range(12)
	th=range(12)
	fn=range(12)
	
	if request.method == 'POST':
		for i in range(12):
			bm[i]=request.POST.get('bm'+str(i+1))
		from  shares.models import bm_list
		q=bm_list(s1=bm[0], s2=bm[1], s3=bm[2], s4=bm[3], s5=bm[4], s6=bm[5], s7=bm[6], s8=bm[7], s9=bm[8], s10=bm[9], s11=bm[10], s12=bm[11])
		q.save()
		for i in range(12):
			cg[i]=request.POST.get('cg'+str(i+1))
		from  shares.models import cg_list
		q=cg_list(s1=cg[0], s2=cg[1], s3=cg[2], s4=cg[3], s5=cg[4], s6=cg[5], s7=cg[6], s8=cg[7], s9=cg[8], s10=cg[9], s11=cg[10], s12=cg[11])
		q.save()
		for i in range(12):
			ig[i]=request.POST.get('ig'+str(i+1))
		from  shares.models import ig_list
		q=ig_list(s1=ig[0], s2=ig[1], s3=ig[2], s4=ig[3], s5=ig[4], s6=ig[5], s7=ig[6], s8=ig[7], s9=ig[8], s10=ig[9], s11=ig[10], s12=ig[11])
		q.save()
		for i in range(12):
			th[i]=request.POST.get('th'+str(i+1))
		from  shares.models import th_list
		q=th_list(s1=th[0], s2=th[1], s3=th[2], s4=th[3], s5=th[4], s6=th[5], s7=th[6], s8=th[7], s9=th[8], s10=th[9], s11=th[10], s12=th[11])
		q.save()
		for i in range(12):
			fn[i]=request.POST.get('fn'+str(i+1))
		from  shares.models import fn_list
		q=fn_list(s1=fn[0], s2=fn[1], s3=fn[2], s4=fn[3], s5=fn[4], s6=fn[5], s7=fn[6], s8=fn[7], s9=fn[8], s10=fn[9], s11=fn[10], s12=fn[11])
		q.save()




	from  shares.models import bm_list
	#bm=['1','2','3','4','5','6','7','8','9','10','11','12']
	#q=bm_list(s1=bm[0], s2=bm[1], s3=bm[2], s4=bm[3], s5=bm[4], s6=bm[5], s7=bm[6], s8=bm[7], s9=bm[8], s10=bm[9], s11=bm[10], s12=bm[11])
	#q.save()
	from  shares.models import cg_list
	#cg=['1','2','3','4','5','6','7','8','9','10','11','12']
	#q=cg_list(s1=cg[0], s2=cg[1], s3=cg[2], s4=cg[3], s5=cg[4], s6=cg[5], s7=cg[6], s8=cg[7], s9=cg[8], s10=cg[9], s11=cg[10], s12=cg[11])
	#q.save()
	from  shares.models import ig_list
	#ig=['1','2','3','4','5','6','7','8','9','10','11','12']
	#q=ig_list(s1=ig[0], s2=ig[1], s3=ig[2], s4=ig[3], s5=ig[4], s6=ig[5], s7=ig[6], s8=ig[7], s9=ig[8], s10=ig[9], s11=ig[10], s12=ig[11])
	#q.save()
	from  shares.models import th_list
	#th=['1','2','3','4','5','6','7','8','9','10','11','12']
	#q=th_list(s1=th[0], s2=th[1], s3=th[2], s4=th[3], s5=th[4], s6=th[5], s7=th[6], s8=th[7], s9=th[8], s10=th[9], s11=th[10], s12=th[11])
	#q.save()
	from  shares.models import fn_list
	#fn=['1','2','3','4','5','6','7','8','9','10','11','12']
	#q=fn_list(s1=fn[0], s2=fn[1], s3=fn[2], s4=fn[3], s5=fn[4], s6=fn[5], s7=fn[6], s8=fn[7], s9=fn[8], s10=fn[9], s11=fn[10], s12=fn[11])
	#q.save()

	bm_list_n=bm_list.objects.all()
	n=len(bm_list_n)
	bm_list_=bm_list.objects.get(id=n)
	cg_list_=cg_list.objects.get(id=n)
	ig_list_=ig_list.objects.get(id=n)
	th_list_=th_list.objects.get(id=n)
	fn_list_=fn_list.objects.get(id=n)
		
	bm_list_=[bm_list_.s1,bm_list_.s2,bm_list_.s3,bm_list_.s4,bm_list_.s5,bm_list_.s6,bm_list_.s7,bm_list_.s8,bm_list_.s9,bm_list_.s10,bm_list_.s11,bm_list_.s12]
	cg_list_=[cg_list_.s1,cg_list_.s2,cg_list_.s3,cg_list_.s4,cg_list_.s5,cg_list_.s6,cg_list_.s7,cg_list_.s8,cg_list_.s9,cg_list_.s10,cg_list_.s11,cg_list_.s12]
	ig_list_=[ig_list_.s1,ig_list_.s2,ig_list_.s3,ig_list_.s4,ig_list_.s5,ig_list_.s6,ig_list_.s7,ig_list_.s8,ig_list_.s9,ig_list_.s10,ig_list_.s11,ig_list_.s12]
	th_list_=[th_list_.s1,th_list_.s2,th_list_.s3,th_list_.s4,th_list_.s5,th_list_.s6,th_list_.s7,th_list_.s8,th_list_.s9,th_list_.s10,th_list_.s11,th_list_.s12]
	fn_list_=[fn_list_.s1,fn_list_.s2,fn_list_.s3,fn_list_.s4,fn_list_.s5,fn_list_.s6,fn_list_.s7,fn_list_.s8,fn_list_.s9,fn_list_.s10,fn_list_.s11,fn_list_.s12]

	
	
	return render_to_response('shares/_shares.html', locals())
	#return HttpResponse('hello it is a page_share')

def lab(request):
	PIPE = subprocess.PIPE
	p=subprocess.Popen(['/srv/vhosts/mysite/scripts/lab.py',])
	#p.wait()
	
	return HttpResponse(p)














