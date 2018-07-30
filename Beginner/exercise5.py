class Display:
    def __init__(self):
        self.s=''
    def getString(self):
        self.s=input()
    def printString(self):
        print(self.s.upper())

d=Display()
d.getString()
d.printString()
