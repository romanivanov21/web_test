from django.conf.urls import include, url
from prices import views

urlpatterns = [
	url( r'generic/$', views.generic ),
	url( r'cat/$', views.categoryes ),
]
