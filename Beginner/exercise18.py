import re

inp=input()
l=[]
l=inp.split(',')
val=[]

for a in l:
    if len(a)<6 and len(a)>12:
        continue
    elif not re.search("[0-9]",a):
        continue
    elif not re.search("[a-z]",a):
        continue
    elif not re.search("[A-Z]",a):
        continue
    elif not re.search("[$@#]",a):
        continue
    elif not re.search("[0-9]",a):
        continue
    val.append(a)

print(val)
