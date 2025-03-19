amount=int(input('Enter the amount: '))
currency= str(input('Choose the currency:AZN, USD or EUR: ')).upper()
convertion= str(input('Choose the currency for convertion:AZN, USD or EUR: ')).upper()
if currency == 'AZN' and convertion == 'USD':
    print(amount * 0.59)
elif currency == 'AZN' and convertion == 'EUR':
    print(amount * 0.51)
elif currency == 'USD' and convertion == 'AZN':
    print(amount * 1.41)
elif currency == 'USD' and convertion == 'EUR':
    print(amount * 0.85)
elif currency == 'EUR' and convertion == 'AZN':
    print(amount * 1.49)
elif currency == 'EUR' and convertion == 'USD':
    print(amount * 1.15)
elif currency == convertion:
    print(amount)
else:
    print(False)