#Pythonic way
l=map(lambda x:x**2, range(1,21))

#layman methord 
def av(a,b):
  l=[]
  for i in range(a,b):
    x=i**2
    l.append(x)
   print(l)
av(12,30)
