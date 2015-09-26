from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def generic( request ) :
	return HttpResponse(u'prices views')

