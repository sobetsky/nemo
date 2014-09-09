from django.db import models

# Create your models here.


class indexs_list(models.Model):
	s=models.CharField(max_length=5)

class bm_list(models.Model):
	s1=models.CharField(max_length=5)
	s2=models.CharField(max_length=5)
	s3=models.CharField(max_length=5)
	s4=models.CharField(max_length=5)
	s5=models.CharField(max_length=5)
	s6=models.CharField(max_length=5)
	s7=models.CharField(max_length=5)
	s8=models.CharField(max_length=5)
	s9=models.CharField(max_length=5)
	s10=models.CharField(max_length=5)
	s11=models.CharField(max_length=5)
	s12=models.CharField(max_length=5)

class cg_list(models.Model):
	s1=models.CharField(max_length=5)
	s2=models.CharField(max_length=5)
	s3=models.CharField(max_length=5)
	s4=models.CharField(max_length=5)
	s5=models.CharField(max_length=5)
	s6=models.CharField(max_length=5)
	s7=models.CharField(max_length=5)
	s8=models.CharField(max_length=5)
	s9=models.CharField(max_length=5)
	s10=models.CharField(max_length=5)
	s11=models.CharField(max_length=5)
	s12=models.CharField(max_length=5)

class ig_list(models.Model):
	s1=models.CharField(max_length=5)
	s2=models.CharField(max_length=5)
	s3=models.CharField(max_length=5)
	s4=models.CharField(max_length=5)
	s5=models.CharField(max_length=5)
	s6=models.CharField(max_length=5)
	s7=models.CharField(max_length=5)
	s8=models.CharField(max_length=5)
	s9=models.CharField(max_length=5)
	s10=models.CharField(max_length=5)
	s11=models.CharField(max_length=5)
	s12=models.CharField(max_length=5)

class th_list(models.Model):
	s1=models.CharField(max_length=5)
	s2=models.CharField(max_length=5)
	s3=models.CharField(max_length=5)
	s4=models.CharField(max_length=5)
	s5=models.CharField(max_length=5)
	s6=models.CharField(max_length=5)
	s7=models.CharField(max_length=5)
	s8=models.CharField(max_length=5)
	s9=models.CharField(max_length=5)
	s10=models.CharField(max_length=5)
	s11=models.CharField(max_length=5)
	s12=models.CharField(max_length=5)

class fn_list(models.Model):
	s1=models.CharField(max_length=5)
	s2=models.CharField(max_length=5)
	s3=models.CharField(max_length=5)
	s4=models.CharField(max_length=5)
	s5=models.CharField(max_length=5)
	s6=models.CharField(max_length=5)
	s7=models.CharField(max_length=5)
	s8=models.CharField(max_length=5)
	s9=models.CharField(max_length=5)
	s10=models.CharField(max_length=5)
	s11=models.CharField(max_length=5)
	s12=models.CharField(max_length=5)

class main_list(models.Model):
	bm=models.ManyToManyField(bm_list)
	cg=models.ManyToManyField(cg_list)
	ig=models.ManyToManyField(ig_list)
	th=models.ManyToManyField(th_list)
