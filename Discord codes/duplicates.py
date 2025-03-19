numbers= input().split()
list=[]
for i in numbers:
    if i not in list:
        list.append(i)
print(list)