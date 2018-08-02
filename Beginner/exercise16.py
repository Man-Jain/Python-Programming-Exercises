inp=input()

l=[int(a)*int(a) for a in inp.split(',') if int(a)%2!=0]

print(l)
