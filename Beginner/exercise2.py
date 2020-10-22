#taking input as "n"
n=int(input())

# taking n= ans
ans=n
#appling loop for n
while n>1:
    
    #setting conditon for n
    n-=1
    # appling new condition
    ans=ans*(n)
    
    #printing ans
print(ans)
