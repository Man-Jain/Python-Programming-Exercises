l=[1,2,3,4,5,6,7,8,9,10]

p=map(lambda x:x**2,filter(lambda x: x%2==0, l))

print(list(p))
