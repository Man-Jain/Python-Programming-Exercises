val=[]
inp=[]
d={'D':0,'W':0}
while True:
    inp=input()
    if not inp:
        break
    val.append(inp)

for a in val:
    inp=a.split(' ')
    if inp[0]=='D':
        d['D']+=int(inp[1])
    elif inp[0]=='W':
        d['W']+=int(inp[1])

ans=d['D']-d['W']

print(ans)
