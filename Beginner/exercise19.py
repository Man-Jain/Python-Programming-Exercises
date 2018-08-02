val=[]
while True:
    inp=input()
    if not inp:
        break
    val.append(tuple(inp.split(',')))

print(sorted(val))
