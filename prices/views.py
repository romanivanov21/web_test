from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

# Create your views here.

def generic( request ) :
	return HttpResponse(u'prices views')

def categoryes( request ) :
	catlist = []
	return render_to_response( u'category.html', locals() )