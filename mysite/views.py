from django.shortcuts import render

from django.http import HttpResponse,Http404
from mysite.cricbuzz import Cricbuzz
from mysite.forms import *
from . import gen as ge

from mysite.models import *

def index(request):
	return	render(request,'mysite/homepage/index.html')

def livescore(request):
	c = Cricbuzz()
	dic= {}
	matches = c.matches()
	if not matches:
		return HttpResponse("can't connect to cricbzz.com......")
	for match in matches:
		#print (match)
		if(match['matchstate'] != 'nextlive'):
			#print (dic)
			dic[match['id']] = (c.livescore(match['id']))
			#print (c.commentary(match['id']))
			#print (c.scorecard(match['id']))
	#print(dic)
	return render(request,'mysite/Livescore/livescore.html',{'matches':dic})

#def livematch(request,mid):
#	return render(request,'')


def compare(request):
	if request.method == 'GET':
		dit = {}
		p_dict = {}
		if 'player1' in request.GET:
			player1 = request.GET['player1']
			player1 = Player.objects.get(name=player1)			 		
			values = player1.get_attrb()
			p_dict = {
			'name':values[0],'team':values[12],'Runs':values[1],'fiftys':values[2],'hundreds':values[3],'matchplayed':values[4],'average':values[5],
			'run_rate':values[6],'HighScore':values[7],'overs':values[8],'wickets':values[9],'economy':values[10],'wicket_streak':values[11]
			}
			print(p_dict)
			dit['player1'] = p_dict
		if 'player2' in request.GET:
			if request.GET['player2']:
				player2 = request.GET['player2']
				print(player2)
				player2 = Player.objects.get(name=player2)			 		
				values = player2.get_attrb()
				p_dict = {
				'name':values[0],'team':values[12],'Runs':values[1],'fiftys':values[2],'hundreds':values[3],'matchplayed':values[4],'average':values[5],
				'run_rate':values[6],'HighScore':values[7],'overs':values[8],'wickets':values[9],'economy':values[10],'wicket_streak':values[11]
				}
				print(p_dict)
				dit['player2'] = p_dict
		if 'player3' in request.GET:
			if request.GET['player3']:
				player3 = request.GET['player3']
				print(player3)
				player3 = Player.objects.get(name=player3)			 		
				values = player3.get_attrb()
				p_dict = {
				'name':values[0],'team':values[12],'Runs':values[1],'fiftys':values[2],'hundreds':values[3],'matchplayed':values[4],'average':values[5],
				'run_rate':values[6],'HighScore':values[7],'overs':values[8],'wickets':values[9],'economy':values[10],'wicket_streak':values[11]
				}
				print(p_dict)
				dit['player3'] = p_dict
		if 'player4' in request.GET and request.GET['player4']:
			if request.GET['player4']:
				player4 = request.GET['player4']
				player4 = Player.objects.get(name=player4)			 		
				values = player4.get_attrb()
				p_dict = {
				'name':values[0],'team':values[12],'Runs':values[1],'fiftys':values[2],'hundreds':values[3],'matchplayed':values[4],'average':values[5],
				'run_rate':values[6],'HighScore':values[7],'overs':values[8],'wickets':values[9],'economy':values[10],'wicket_streak':values[11]
				}
				print(p_dict)
				dit['player4'] = p_dict
	return render(request,'mysite/Compare.html',dit)		

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
	try:
		p = Player.objects.get(name=player_name)
		values = p.get_attrb()
		player_dict = {
		'name':values[0],'team':values[12],'Runs':values[1],'fiftys':values[2],'hundreds':values[3],'matchplayed':values[4],'average':values[5],
		'run_rate':values[6],'HighScore':values[7],'overs':values[8],'wickets':values[9],'economy':values[10],'wicket_streak':values[11]
		}
		return render(request,'mysite/player/player.html',player_dict)
	except Player.DoesNotExist:
		raise Http404("Player does not Exist.....")

#def team(request):
	
def about(request):
	return render(request,'mysite/about.html',{'about':'About Us','news':['We are a gang of two people','who steal scores from cricbuzz.']})

#	return	

