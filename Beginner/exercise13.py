input_sentence=input()
c=0
n=0

for a in input_sentence:
    if (ord(a)>=65 and ord(a)<=90) or (ord(a)>=97 and ord(a)<=122):
        c+=1
    elif int(a)>=0 and int(a)<=9:
        n+=1

print(c,' ',n)
