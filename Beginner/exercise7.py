rc=input()
l=[]
l=rc.split(',')
print(l)
row=int(l[0])
col=int(l[1])
arr=[]
tmp=[]
for a in range(row):
    tmp=[]
    for b in range(col):
        tmp.append(a*b)
    arr.append(tmp)

print(arr)
