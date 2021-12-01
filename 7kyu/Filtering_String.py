def filter_list(l):
    l1 = []
    n = len(l)
    for i in range(0,n):
        p = l[i]
        ele = isinstance(p,int)
        if ele == True:
            l1.append(p)
        else:
            continue
    return l1 