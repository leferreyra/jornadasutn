#encoding:utf-8
from django.db import models
from tinymce.models import HTMLField

class Auspiciante(models.Model):
	
	nombre = models.CharField(max_length=50)
	imagen = models.ImageField(upload_to='auspiciantes', verbose_name='Imágen')
	link = models.CharField(max_length=100, blank=True)

	def __unicode__(self):
		return self.nombre


class Organizador(models.Model):
	
	nombre = models.CharField(max_length=50)
	imagen = models.ImageField(upload_to='organizadores', verbose_name='Imágen')

	def __unicode__(self):
		return self.nombre

class Jornada(models.Model):
	
	nombre = models.CharField(max_length=50)
	logo = models.ImageField(upload_to='logos', verbose_name='Logo')
	fecha = models.DateTimeField()
	programa = HTMLField()
	iframe_transmision = models.TextField(blank=True)
	organizadores = models.ManyToManyField(Organizador)
	auspiciantes = models.ManyToManyField(Auspiciante)

	def __unicode__(self):
		return self.nombre
