def sort_by_length(arr):
    l = []
    n = []
    for i in range(0,len(arr)):
        l.append(len(arr[i]))
    
    for j in range(0,len(arr)):
        a = l.index(min(l))
        n.append(arr[a])
        l[a] = l[a] + 30
    
    return(n)
