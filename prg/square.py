n=int(input('enter the number of elements :'))
num_list=[]
for i in range(n):
    a=int(input('enter the numbers :'))
    num_list.append(a)
print('entered list:',num_list)
sqr_lst=[x**2 for x in num_list]
print('squared list',sqr_lst)