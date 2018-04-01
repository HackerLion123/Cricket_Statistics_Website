from django.shortcuts import render

from django.http import HttpResponse,Http404

from mysite.cricbuzz import Cricbuzz

from . import gen as ge

from mysite.models import *

def index(request):
	return	render(request,'mysite/index.html')

def livescore(request):
	c = Cricbuzz()
	dic= {}
	matches = c.matches()
	for match in matches:
		#print (match)
		if(match['matchstate'] != 'nextlive'):
			#print (dic)
			dic[match['id']] = (c.livescore(match['id']))
			#print (c.commentary(match['id']))
			#print (c.scorecard(match['id']))
	print(dic)
	return render(request,'mysite/Livescore/livescore.html',{'matches':dic})

#def livematch(request,mid):
#	return render(request,'')

def matches(request):
	match = Match.objects.all()
	matchs_dict = {'matches':match}
	return	render(request,'mysite/match/matches.html',matchs_dict)

def match(request,pk):
	try:
		obj = Match.objects.get(id=pk)
		values = obj.get_attrb()
		match_dict = {'team1':values[0],'team2':values[1],'type':values[2],'batting1':values[3].get_attrb(),'batting2':values[4].get_attrb(),'bowling1':values[5].get_attrb(),'bowling2':values[6].get_attrb()}
		c = ge.Statistics()
		c.generate()
		return render(request,'mysite/match/match.html',match_dict)
	except Match.DoesNotExist:
		raise Http404("Match does not Exist.....")

def getScores(request):
	pass;

def player(request,player_name):
	p = Player.objects.get(name=player_name)
	values = p.get_attrb()
	player_dict = {
	'name':values[0],'team':values[12],'Runs':values[1],'fiftys':values[2],'hundreds':values[3],'matchplayed':values[4],'average':values[5],
	'run_rate':values[6],'HighScore':values[7],'overs':values[8],'wickets':values[9],'economy':values[10],'wicket_streak':values[11]
	}
	return render(request,'mysite/player/player.html',player_dict)
	
#def team(request):
	
#def about(request):
#	return render(request,'about.html')

#	return	

