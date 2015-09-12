# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

#controller for hello world
def hello( request ) : 
	return HttpResponse(u'Hello')

#controller return current datatime 
def cur_datetime( request, offset ) :
	try :
		curdate = datetime.datetime.now()
		offset = int(offset)
		#offset = 10
		if offset < -12 or offset > 12 :
			raise Http404
		delta = datetime.timedelta( hours = offset )
		curdate += delta
		return render_to_response( 'curdate.html', locals())
	except ValueError:
		raise Http404