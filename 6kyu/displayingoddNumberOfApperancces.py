def arr(n):
    c = 0
    l = []
    for i in range(0,len(n)):
        a = n[i]
        for j in range(0,len(n)):
            b = n[j]
            if a == b:
                c += 1
            else:
                continue
        if c % 2 != 0:
            l.append(a)
        c = 0
    return set(l)
print(arr([1,1,2,4,2,4,1,7,7,2,5,7,2,4,8,3,5]))

#alter solun:
def find_it(seq):
    n = len(seq)
    for i in range(0,n):
        if (seq.count(seq[i])) %2 != 0:
            return seq[i]
        else:
            continue