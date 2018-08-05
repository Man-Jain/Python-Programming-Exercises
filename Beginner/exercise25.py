class Square:
    num='7'
    def __init__(self,num):
        self.num="9"
        print(num)
        print(self.num)

s=Square(5)
print(Square.num)
