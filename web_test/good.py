# -*- coding: utf-8 -*-

class Good( object ) :
	def __init__( self, name, price, unit) :
		self.__Name  = unicode( name  )
		self.__Price = float  ( price )
		self.__Unit  = unicode( unit  )

	name  = property( lambda self : self.__Name )
	price = property( lambda self : self.__Price)
	unit  = property( lambda self : self.__Unit )

	def uint_to_kg( self ) :
		self.__Unit = u'kg'
		return self.__Price

	uint_to_kg.alters_data = True #запрещает uint_to_kg метод вызывать из шаблона
	