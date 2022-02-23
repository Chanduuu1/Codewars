def highest_rank(arr):
    n = []
    m = []
    final = []
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
            else:
                continue
        n.append(arr[i])
        m.append(count)
    maxx = max(m)
    for i in range(len(m)):
        if m[i] == maxx:
            final.append(n[i])            
        else:
            continue
    return max(final)