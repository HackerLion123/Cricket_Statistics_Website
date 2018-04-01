from cricbuzz import Cricbuzz

c = Cricbuzz()
matches = c.matches()
for match in matches:
	print (match)
	if(match['matchstate'] != 'nextlive'):
		print (c.livescore(match['id']))
		#print (c.commentary(match['id']))
		#print (c.scorecard(match['id']))
