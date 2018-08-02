inp=input()
d={'upper':0,'lower':0}

for a in inp:
    if ord(a)>=65 and ord(a)<=90:
        d['upper']+=1
    elif ord(a)>=97 and ord(a)<=122:
        d['lower']+=1

print(d['upper'],' ',d['lower'])
