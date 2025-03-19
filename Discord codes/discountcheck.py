total= int(input())
if total >= 1000:
    discount = total * 0.1
    print('discount available:', discount)
else:
    print('discount unsustainable', total)