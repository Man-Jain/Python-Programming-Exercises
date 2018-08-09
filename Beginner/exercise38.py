t1=(1,2,3,4,5,6,7,8,9,10)
t2=[]
l=()
for a in t1:
    if(a%2==0):
        t2.append(a)
l=tuple(t2)
print(l)
