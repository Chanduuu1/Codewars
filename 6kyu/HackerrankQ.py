from collections import Counter

''' getting and storing names and marks '''
main = []
temp  = []
n = int(input())
for i in range(n):
    name = input()
    temp.append(name)
    mark = float(input())
    temp.append(mark)
    main.append(temp)
    temp = []
    

''' Finding 2nd lowest marks'''
for i in range(n):
    temp.append(main[i][1])

e = Counter(temp)
val = min(temp)
if e[val] >= 2:
    b = e[val]
    while b != 0:
        ind1 = temp.index(min(temp))
        temp.remove(min(temp))
        main.remove(main[ind1])
        b -= 1
else:
    ind1 = temp.index(min(temp))
    temp.remove(min(temp))
    main.remove(main[ind1])

nList = []
d = Counter(temp)
val2 = min(temp)
if d[val2] >= 2:
    b = d[val2]
    while b != 0:
        ind2 = temp.index(val2)
        nList.append(main[ind2][0])
        temp.remove(val2)
        main.remove(main[ind2])
        b-=1
else:
    ind2 = temp.index(min(temp))
    nList.append(main[ind2][0])

nList.sort()
for i in nList:
    print(i)