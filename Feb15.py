class Traveller:
	def __init__(self,name,country,age,countryfrom):
		self.name=name
		self.country=country
		self.age=age
		self.countryfrom=countryfrom
class Travelagency:
	def __init__(self,t_list):
		self.t_list=t_list
	def count_travelled_country(self,search):
		cnt=0
		for i in self.t_list:
			for j in i.country:
				if j==search:
					cnt+=1
		return cnt
	def get_max_travelled(self):
		max0=0
		nam=""
		for j in self.t_list:
			if(len(j.country)>max0):
				max0=len(j.country)
				nam=j.name
		return nam
n = int(input())
t_list=[]
for i in range(n):
	name=str(input())
	m=int(input())
	country=[]
	for j in range(m):
		country.append(str(input()))
	age=int(input())
	countryfrom=str(input())
	t_list.append(Traveller(name,country,age,countryfrom))
search=str(input())
obj=Travelagency(t_list)
print(obj.count_travelled_country(search))
print(obj.get_max_travelled())
