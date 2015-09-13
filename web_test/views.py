# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from web_test.good import Good
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
		Good ( name = u'Котлеты по-киевски',   price = 80.0,  unit = u'шт.'   ),
		Good ( name = u'Котлеты по-москGоски', price = 95.70, unit = u'шт.'   ),
		Good ( name = u'Макароны',             price = 20.0,  unit = u'гр.'   ),
		Good ( name = u'Суп',                  price = 55.0,  unit = u'порция'),
	]
	return render_to_response( 'price_lists.html', locals() )