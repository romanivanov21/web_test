from django.db import models
import datetime
import random

# Create your models here.

def default_slug() :
	Dt = datetime.datetime.now()
	return u's%04d%02d%02d%02d%02d%02d%03d' % (
			Dt.year, Dt.month, Dt.day, 
			Dt.hour, Dt.minute, Dt.second, random.randint(0,999) )

class Category( models.Model ) : 
	slug  =  models.SlugField( unique = True, default = default_slug)
	name  =  models.TextField()
	
	def __unicode__( self ) :
		return self.name

class Meta :
	verbose_name = u'Category'
	verbose_name_plural = u'Categoryes'
	ordering = [u'name']

class Tag( models.Model ) :
	slug  =  models.SlugField( unique = True, default = default_slug )
	name  =  models.TextField( unique = True )

	def __unicode__( self ) :
		return self.name

class Unit( models.Model ) :
	name  =  models.TextField()

	def __unicode__( self ) :
		return self.name

class Lang( models.Model ) :
	code  =  models.CharField( max_length = 3, primary_key = True)
	name  =  models.TextField()

	def __unicode__( self ) :
		return self.code + u'----' + self.name

class Good( models.Model ) :
	slug  =  models.SlugField( unique = True, default = default_slug )
	name  =  models.TextField()
	price =  models.DecimalField( max_digits = 22, decimal_places = 2 )
	unit  =  models.ForeignKey( Unit )
	cath  =  models.ForeignKey( Category )
	tags  =  models.ManyToManyField( Tag )
	langs =  models.ManyToManyField( Lang )

	def __unicode__( self ) :
		return self.name

