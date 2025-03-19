def majorityelement(lst):
    maxelement = None
    n = len(lst)
    for i in lst:
        if lst.count(i) > n // 2:
            maxelement = i
            break
    return maxelement
print(majorityelement([3, 3, 4, 2, 3, 3, 3])) 