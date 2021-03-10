class Players:
	def __init__(self,name,country,matches,runs,wickets):
		self.name=name
		self.country=country
		self.matches=matches
		self.runs=runs
		self.wickets=wickets
class Team:
	def __init__(self,l_list):
		self.l_list=l_list
	def min_runs(self,run):
		for i in self.l_list:
			if(i.runs==run):
				print(i.name)
				print(i.runs)
				print(i.country)
				break
	def max_wickets(self,wicket):
		for i in self.l_list:
			if(i.wickets==wicket):
				print(i.name)
				print(i.wickets)
				print(i.country)
				break
n=int(input())
wicket=0
run=9999999999
l_list=[]
for i in range(n):
	name=str(input())
	country=str(input())
	matches=int(input())
	runs=int(input())
	if(runs<run):
		run=runs
	wickets=int(input())
	if(wickets>wicket):
		wicket=wickets
	l_list.append(Players(name,country,matches,runs,wickets))
obj=Team(l_list)
obj.min_runs(run)
obj.max_wickets(wicket)
	
