# taking input as ïnput_number"
input_numbers=input()
# '1,2,3'
input_list=input_numbers.split(',') # ['1','2','3']

#making a new list 
div_lst=[]

#applying loop in splitted input list 
for a in input_list:
    
    # checking the divisibulity by 5
    if int(a,2)%5==0:
        #appending if the above condition is true
        div_lst.append(a)
        
#printing the new list
print(div_lst)
