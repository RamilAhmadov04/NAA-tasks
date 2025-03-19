initdepo = int(input('Enter your initial deposit '))
while True:
    depoaction = input('Enter D for deposit or W for withsraw: ').upper()
    amount = int(input())
    if depoaction == 'D':
        print(initdepo + amount)
    if depoaction == 'W':
        if amount > initdepo:
            print('too much')
        else:
            print(initdepo - amount)