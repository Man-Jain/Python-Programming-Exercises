def max(a,b):
    l1=len(a)
    l2=len(b)
    if l1>l2:
        print(a)
    elif l2>l1:
        print(b)
    else:
        print(a+'\n'+b)

max("Hello","Me")
max("Hello","World")
max("Hello","Morning")
