from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def no_picture( request ) :
	return HttpResponseRedirect(u"/static/not_found.png")