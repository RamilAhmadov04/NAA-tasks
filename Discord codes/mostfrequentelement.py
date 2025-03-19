list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = 0
for num in list:
    for i in list:
        if i == num:
            count += 1
    if count > 0:
        mostfrequent = num
print(mostfrequent) 
