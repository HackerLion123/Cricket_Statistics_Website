from mysite.models import *

""" Class to create/update Player and Team Models """
class Statistics:
	total_score = {}
	def __init__(self):
		self.Match_object = Match.objects.all()

	def player(self):
		print(self.Match_object)
		for match in self.Match_object:
			print(match)
			#match.updated = False
			#match.save()
			if match.updated == False:
				if self.Team(match):
					team_batting = [match.batting1.get_attrb(),match.batting2.get_attrb()]
					self.batting(team_batting[0],match.team1)
					self.batting(team_batting[1],match.team2)
					team_bowling = [match.bowling1.get_attrb(),match.bowling2.get_attrb()]
					self.bowling(team_bowling[0],match.team1)
					self.bowling(team_bowling[1],match.team2)
					match.updated = True
					match.save()
				else:
					print("Error")

	def Team(self,match):
		teams = [match.team1,match.team2]
		(ODI,T20,Test) = (0,0,0)
		for t in teams:
			if t:
				if not Team.objects.filter(name=t):
					if match.match_type == "ODI":
						ODI = 1
					if match.match_type == "T20":
						T20 = 1
					if match.match_type == "Test":
						Test = 1 
					t = Team(t,Test,ODI,T20)
					t.save()
				
				elif Team.objects.filter(name=t):
					t = Team.objects.get(name=t)
					if match.match_type == "Test":
						t.Test_wins += 1
					if match.match_type == "T20":
						t.T20_wins += 1
					if match.match_type == "ODI":
						t.ODI_wins += 1
					t.save()
		return True

	def generate(self):
		self.player()

	def bowling(self,bowl,team):
		for c in bowl:
			if c:
				(c[1],c[2],c[3],c[4]) = (int(c[1]),int(c[2]),int(c[3]),int(c[4]))
				try:
					economy = (c[1]*6)/c[4]
				except ZeroDivisionError as e:
					print(e)
				print (economy)	
				if not Player.objects.filter(name=c[0]):
					overs = c[1]
					wickets = c[2]
					streak = c[2]
					b = Player(name=c[0].lower(),team=Team.objects.get(name=team),matchplayed=1,overs=overs,economy = economy,wickets=wickets,wicket_streak=streak)
					b.save()
				elif Player.objects.filter(name=c[0]):
					b = Player.objects.filter(name=c[0])
					b = b[0]
					b.matchplayed += 1
					if b.overs and b.wickets and b.economy:
						b.overs += c[1]
						b.wickets += c[2]
						if economy < b.economy:
							b.economy = economy
						if c[2] > b.wicket_streak:
							b.wicket_streak = c[2]
					else:
						b.overs = c[1]
						b.wickets = c[2]
						b.economy = economy
						print("diff:"+str(b.economy))
						b.wicket_streak = c[1]
					b.save()

	def batting(self,m,te):
		hundred = 0
		fifty = 0
		score = 0
		over = 0
		for c in m:
			if c:
				if not Player.objects.filter(name=c[0]):
					print(c)	
					(c[1],c[2],c[3]) = (int(c[1]),int(c[2]),int(c[3]))
					runs = c[1]
					score += c[1]
					over += c[2]						
					if c[1] > 50:
						fifty = 1
						if c[1] > 100:
							hundred = 1
					match_played = 1
					averge = c[1]
					try:
						runrate = (c[1]/c[2])*100
					except Exception as e:
						print(e)
					high_score = c[1]
					t = Player(c[0].lower(),te,runs,fifty,hundred,match_played,averge,runrate,high_score)
					t.save()

				elif Player.objects.filter(name=c[0]):
					p = Player.objects.filter(name=c[0])
					p = p[0]
					(c[1],c[2],c[3]) = (int(c[1]),int(c[2]),int(c[3]))
					runs = c[1]
					score += c[1]
					over += c[2]	
					if c[1] > 50:
						fifty = 1
						if c[1] > 100:
							hundred = 1
					try:
						runrate = c[1]/c[2]
					except ZeroDivisionError as e:
						print(e)

					p.matchplayed += 1
					p.Runs += runs
					p.fiftys += fifty 
					p.hundreds +=  hundred
					if runrate > p.run_rate:
						p.run_rate = runrate
					if runs > p.HighScore:
						p.HighScore = runs
					p.save()
				self.total_score[c[0]] = {'total':score,'over':(over//6)}	


"""def generate():
	Match_object = Match.objects.all()
	for match in Match_object:
		#print(match)
		#match.updated = False
		#match.save()
		if match.updated == False:
			team1_batting = [match.batting1.get_attrb(),match.batting2.get_attrb()]
			#team1_batting = Match_object[0].batting2
			for m in team1_batting:
				hundred = 0
				fifty = 0
				for c in m:
					if c:
						if not Player.objects.filter(name=c[0]):
							print(c[0])	
							(c[1],c[2],c[3]) = (int(c[1]),int(c[2]),int(c[3]))						
							if c[1] > 50:
								fifty = 1
								if c[1] > 100:
									hundred = 1
							match_played = 1
							averge = c[1]
							try:
								runrate = (c[1]/c[2])*100
							except Exception as e:
								print(e)
							high_score = c[1]
							t = Player(c[0],runs,fifty,hundred,match_played,averge,runrate,high_score)
							t.save()
							match.updated = True
							match.save()
						elif Player.objects.filter(name=c[0]):
							p = Player.objects.filter(name=c[0])
							p = p[0]
							(c[1],c[2],c[3]) = (int(c[1]),int(c[2]),int(c[3]))
							runs = c[1]	
							if c[1] > 50:
								fifty = 1
								if c[1] > 100:
									hundred = 1
							try:
								runrate = c[1]/c[2]
							except ZeroDivisionError as e:
								print(e)

							p.matchplayed += 1
							p.Runs += runs
							p.fiftys += fifty 
							p.hundreds +=  hundred
							if runrate > p.run_rate:
								p.run_rate = runrate
							if runs > p.HighScore:
								p.HighScore = runs
							p.save()
							match.updated = True
							match.save()"""
							

