from django.db import models

# Create your models here.

class Category( models.Model ) : 
	slug  =  models.SlugField( unique = True )
	name  =  models.TextField()

class Tag( models.Model ) :
	slug  =  models.SlugField( unique = True )
	name  =  models.TextField( unique = True )

class Unit( models.Model ) :
	name  =  models.TextField()

class Lang( models.Model ) :
	code  =  models.CharField( max_length = 3, primary_key = True)
	name  =  models.TextField()

class Good( models.Model ) :
	slug  =  models.SlugField( unique = True )
	name  =  models.TextField()
	price =  models.DecimalField( max_digits = 22, decimal_places = 2 )
	unit  =  models.ForeignKey( Unit )
	cath  =  models.ForeignKey( Category )
	tags  =  models.ManyToManyField( Tag )
	langs =  models.ManyToManyField( Lang )


