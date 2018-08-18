from django.conf.urls import url
from . import views #from current directory
from mysite.models import *
from django.views.generic import ListView,DetailView

urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^mysite/$',views.index,name="index"),
	url(r'^mysite/match/$',views.matches),
	url(r'^mysite/compare/$',views.compare),
	url(r'^mysite/compare/(?P<p1>[\w\s])/(?P<p2>[\w\s])/$',views.compare),
	url(r'^mysite/compare/$',views.compare),
	url(r'^mysite/livescore/$',views.livescore),
	#url(r'^$',ListView.as_view(queryset=Match.objects.all().order_by("-date"))),
	#url(r'^player/$',views),
	url(r'^player/(?P<player_name>[\w\s]+)/$',views.player,name="player"),
	url(r'^match/(?P<pk>[0-9]+)/$',views.match),
]


