from django.conf.urls import url
from . import views #from current directory
from mysite.models import *
from django.views.generic import ListView,DetailView

urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^mysite/index.html$',views.index,name="index"),
	url(r'^mysite/match/matches.html$',views.matches),
	url(r'^mysite/Livescore/livescore.html$',views.livescore),
	#url(r'^$',ListView.as_view(queryset=Match.objects.all().order_by("-date"))),
	#url(r'^player/$',views),
	url(r'^player/(?P<player_name>\w+)/$',views.player,name="player"),
	url(r'^match/(?P<pk>[0-9]+)/$',views.match),
]


