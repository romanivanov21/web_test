# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

#controller for hello world
def hello( request ) : 
	return HttpResponse(u'Hello')

#controller returnet current datatime plus offset
def cur_datetime( request, offset ) :
	try :
		curdate = datetime.datetime.now()
		offset = int(offset)
		#offset = 10
		if offset < -12 or offset > 12 :
			raise Http404
		delta = datetime.timedelta( hours = offset )
		curdate += delta
		return render_to_response( 'curdate.html', locals() )
	except ValueError:
		raise Http404

def prices( request ) :
	title = u'меню:'
	goods = [
		{ 'name': u'Котлеты по-киевски',
		  'price': u'80.0р.',
		  'unit': u'шт.',
		},
		{ 'name': u'Котлеты по-москвоски',
		  'price': u'95.70р.',
		  'unit': u'шт.',
		},
		{ 'name': u'Макароны',
		  'price': u'20.0р.',
		  'unit': u'гр.',
		},
		{ 'name': u'Суп',
		  'price': u'55.0р.',
		  'unit': u'порция',
		},
	]
	return render_to_response( 'price_lists.html', locals() )