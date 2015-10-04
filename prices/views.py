from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from models import Category, Tag, Good

# Create your views here.

def generic( request ) :
	return HttpResponse(u'prices views')

def categoryes( request ) :
	# Views all category
	catlist = Category.objects.all()
	return render_to_response( u'category.html', locals())
	# Views all tags
def tags( request ) :
	taglist = Tag.objects.all()
	return render_to_response( u'tag.html', locals())
def goods( request ) :
	goodlist = Good.objects.all()
	return render_to_response(u'goods.html', locals())
def goods_by_cat( request, cat_slug ) :
	try:
		cat = Category.objects.get( slug = cat_slug )
		goodlist = cat.good_set.all()
		return render_to_response(u'goods_cat.html', locals())
	except Category.DoesNotExist :
		raise Http404
def goods_by_tag( request, tag_slug ) :
	try:
		tag = Tag.objects.get( slug = tag_slug )
		goodlist = tag.good_set.all()
		return render_to_response(u'goods_tag.html', locals())
	except Tag.DoesNotExist:
		raise Http404
def one_good( request, good_slug ) :
	try:
		good = Good.objects.get( slug = good_slug )
		tags = good.tags.all()
		langs = good.langs.all()
		return render_to_response(u'one_good.html', locals())
	except Good.DoesNotExist :
		raise Http404
def new_tag( request ) :
	return render_to_response(u'new_tag.html',locals())
def save_tag( request ) :
	user_agent = request.META['HTTP_USER_AGENT']
	tagname = request.GET['tagname']
	#will to be validate tagname
	tag = Tag( name = tagname )
	tag.save()
	return render_to_response(u'tag_saved.html',locals())