# making an empty list
l=[]

# Applying a loop from 2000 to 3200
for a in range(2000,3201):
    # checking if no is divisable by 7
    # but not by 5
    if a%7==0 and a%5!=0:
        # adding the number after conditions
        l.append(a)

# printing the list
print(l)
