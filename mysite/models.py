from django.db import models

class Team(models.Model):
	name = models.CharField(max_length=120,primary_key=True)
	
	Test_wins = models.IntegerField()
	ODI_wins = models.IntegerField()
	T20_wins = models.IntegerField()
	

	def __str__(self):
		return self.name
	


class Player(models.Model):
	name = models.CharField(max_length=120,primary_key=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE,null=True)

	#Data related to batting - 7
	Runs = models.IntegerField(null=True)
	fiftys = models.IntegerField(null=True)
	hundreds = models.IntegerField(null=True)
	matchplayed = models.IntegerField()
	average = models.IntegerField(null=True)
	run_rate = models.FloatField(null=True)
	HighScore = models.IntegerField(null=True)
	
	#Data related to bowling - 4
	overs = models.IntegerField(null=True)
	wickets = models.IntegerField(null=True)
	economy = models.FloatField(null=True)
	wicket_streak = models.IntegerField(null=True)

	def __str__(self):
		return self.name
	
	def get_attrb(self):
		return [self.name,self.Runs,self.fiftys,self.hundreds,
self.matchplayed,self.average,self.run_rate,self.HighScore,self.overs,self.wickets,self.economy,self.wicket_streak,self.team]
	def get_batting(self):
		return [self.name,self.Runs,self.fiftys,self.hundreds,self.matchplayed,self.average,self.run_rate,self.HighScore]

	def get_bowling(self):
		return [self.overs,self.wickets,self.economy,self.wicket_streak]
	@classmethod
	def create_batsman(cls,a,b,c,d,e,f,g):
		cls.name = a

		#Data related to batting
		cls.fiftys = b
		cls.hundreds = c
		cls.matchplayed = d
		cls.average = e
		cls.run_rate = f
		cls.HighScore = g
		cls.save()
		
	

class Batting_log(models.Model):
	player1 = models.CharField(max_length=120)
	player2 = models.CharField(max_length=120,null=True,blank=True)
	player3 = models.CharField(max_length=120,null=True,blank=True)
	player4 = models.CharField(max_length=120,null=True,blank=True)
	player5 = models.CharField(max_length=120,null=True,blank=True)
	player6 = models.CharField(max_length=120,null=True,blank=True)
	player7 = models.CharField(max_length=120,null=True,blank=True)
	player8 = models.CharField(max_length=120,null=True,blank=True)
	player9 = models.CharField(max_length=120,null=True,blank=True)
	player10 = models.CharField(max_length=120,null=True,blank=True)
	player11 = models.CharField(max_length=120,null=True,blank=True)
	
	def get_attrb(self):
		return [
			self.player1.split(),self.player2.split(),self.player3.split(),self.player4.split(),self.player5.split(),self.player6.split(),
			self.player7.split(),self.player8.split(),self.player9.split(),self.player10.split(),self.player11.split()
		]

class Bowling_log(models.Model):
	player1 = models.CharField(max_length=120)
	player2 = models.CharField(max_length=120,null=True,blank=True)
	player3 = models.CharField(max_length=120,null=True,blank=True)
	player4 = models.CharField(max_length=120,null=True,blank=True)
	player5 = models.CharField(max_length=120,null=True,blank=True)
	

	def get_attrb(self):
		return [self.player1.split(),self.player2.split(),self.player3.split(),self.player4.split(),self.player5.split()]

class Match(models.Model):
	team1 =  models.CharField(max_length=120)
	team2 = models.CharField(max_length=120)
	match_type = models.CharField(max_length=120)
	updated = models.BooleanField(default=False)

	batting1 = models.ForeignKey(Batting_log,related_name='batting1',on_delete=models.CASCADE,null=True)
	batting2 = models.ForeignKey(Batting_log,related_name='batting2', on_delete=models.CASCADE,null=True)

	bowling1 = models.ForeignKey(Bowling_log,related_name='bowling1',on_delete=models.CASCADE,null=True)
	bowling2 = models.ForeignKey(Bowling_log,related_name='bowling2',on_delete=models.CASCADE,null=True)

	date = models.DateField()

	def __str__(self):
		return self.team1+" vs "+self.team2  
	
	def get_attrb(self):
		return [self.team1,self.team2,self.match_type,self.batting1,self.batting2,self.bowling1,self.bowling2,self.date]


