input_numbers=input()
input_list=[x for x in input_numbers.split(',')]
div_lst=[]

for a in input_list:
    if int(a,2)%5==0:
        div_lst.append(a)

print(div_lst)
