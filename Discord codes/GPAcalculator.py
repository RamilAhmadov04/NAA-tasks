total_GPA = 0
point = 0
for i in range(5):
    grade= str(input('Put a grade:A,B,C,D or F: ')).upper()
    if grade == 'A':
        point == 5
    elif grade == 'B':
        point == 4
    elif grade == 'C':
        point == 3
    elif grade =='D':
        point == 2
    elif grade == 'F':
        point == 1
    else:
        print('error')
total_GPA += point 
print(total_GPA/5)
