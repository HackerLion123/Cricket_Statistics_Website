from mysite.models import *

def generate():
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
							match.save()
							

