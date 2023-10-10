t1=(1,2,3)
t2=(4,5,6)
list1=list(t1+t2)
print(list1)
t1=t1[::-1]
t2=t2[::-1]
t_result=list1, t1, t2
print(t_result)
findex=t_result[0][2]
sindex=t_result[1][2]
tindex=t_result[2][2]
print(findex, "\n",sindex,"\n",tindex)