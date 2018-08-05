inp=input()
lst=[a for a in inp.split(' ')]
d={}

for i in lst:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for i in d.keys():
    print(i+": "+str(d[i]))
