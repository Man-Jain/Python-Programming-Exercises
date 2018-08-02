class Generator:
    def __init__(self):
        pass
    def div(self,n):
        self.lst=[]
        for a in range(1,n+1):
            if a%7==0:
                self.lst.append(a)
        return self.lst

p=[]
a=Generator()
p=a.div(100)

print(p)
