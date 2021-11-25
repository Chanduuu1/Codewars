def is_isogram(s):
    n=len(s)
    st = s.lower()
    if n>0:
        for i in range(0,n):
            a = st[i]
            for j in range(0,n):
                b = st[j]
                if (a == b and i != j):
                    return False
                elif (a!=b and i == n-1):
                    return True
                else:
                    continue
    else:
        return True