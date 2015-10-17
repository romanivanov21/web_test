from django.conf.urls import include, url
from prices import views

urlpatterns = [
	url( r'generic/$', views.generic ),
	url( r'cat/$', views.categoryes ),
	url( r'cat/([a-zA-Z0-9]+)/$', views.goods_by_cat),
	url( r'tag/([a-zA-Z0-9]+)/$', views.goods_by_tag),
	url( r'good/([a-zA-Z0-9]+)/$', views.one_good),
	url( r'newtag/$', views.new_tag), 
	url( r'save_tag/$', views.save_tag),
	url( r'tag/$', views.tags),
	url( r'newgood/$',views.new_good),
	url( r'save_good/$', views.save_good),
	url( r'good/$', views.goods),
	url( r'login/$', views.login),
]
