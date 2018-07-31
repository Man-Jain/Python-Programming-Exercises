import math

l=[]
inp=str(input())
l=inp.split(',')
print(l)
ans=[]
C=50
H=30
for D in l:
    answ=math.sqrt((2*C*int(D))/H)
    ans.append(round(answ))
print(ans)
