val=[]
tmp=[]

for a in range(1000,3001):
    s=str(a)
    for b in s:
        if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
            c=1
        else:
            c=0
    if c==1:
        val.append(a)

print(val)

