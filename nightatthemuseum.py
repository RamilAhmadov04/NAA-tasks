word = list(input())
sum= 0 ; distance = 0
cycle = int(len(word))
for el in range(cycle):
    if el + 1 == cycle:
        break
    else:
        let1 = word[el]
        let2 = word[el+1]
        distance = abs(ord(let1) - ord(let2))
        if distance < 14:
            sum += distance
        else:
            sum += 26 - distance
        distance = 0
print(sum)

   