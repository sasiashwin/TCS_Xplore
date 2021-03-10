class Container:
	def __init__(self,ids,length,breadth,height,price):
		self.ids=ids
		self.length=length
		self.breadth=breadth
		self.height=height
		self.price=price
	def find_volume(length,breadth,height):
		return length*height*breadth
class Packaging_Company:
	def __init__(self,l_list):
		self.l_list=l_list
	def find_ContainerCost(self,find):
		for i in self.l_list:
			if(i.ids==find):
				return Container(i.length,i.breadth,i.height)*i.price
		return 0
	def find_largest_container(self):
		m=0
		isi=0
		for i in self.l_list:
			v=i.length*i.breadth*i.height
			if(v>m):
				m=v
				isi=i.ids
		return isi,m
n=int(input())
l_list=[]
for i in range(n):
	ids=int(input())
	length=int(input())
	breadth=int(input())
	height=int(input())
	price=int(input())
	l_list.append(Container(ids,length,breadth,height,price))
find=int(input())
obj=Packaging_Company(l_list)
if(obj.find_ContainerCost(find)!=0):
	print(obj.find_ContainerCost(find))
else:
	print("no containers found")
ids,m=obj.find_largest_container()
print(ids,end=" ")
print(m)

