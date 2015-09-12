# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404

def hello( request ) : 
	return HttpResponse(u'Hello')
