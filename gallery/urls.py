from django.conf.urls import include, url
from gallery import views


urlpatterns = [
	url( r'.*\.jpe?g/$', views.no_picture ),
]
