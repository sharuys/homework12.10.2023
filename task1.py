list1=input("Введіть рядок із 15 символів: ")
if not list1:
    print("Введіть ще раз")
elif len(list1)<15:
    while len(list1)<15:
        list1=list1*3
        list2=list(list1)
else:
    list2=list1
print("Повний список: ",list2)
res1=list2[-5:]
print("Останні 5 елементів зі списку: ", res1)
res2=list2[::-1]
print("У зворотньому порядку: ", res2)
res3=list2[::2]
print("З парними індексами: ", res3)
last5=list2[-5:]
first5=list2[5:]
list2=last5+first5
print(list2)