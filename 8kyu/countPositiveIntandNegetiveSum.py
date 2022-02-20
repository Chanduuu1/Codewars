def count_positives_sum_negatives(arr):
    a = 0
    sum = 0
    m = []
    if len(arr)>0:
        for i in range(len(arr)):
            if arr[i] > 0:
                a +=1
            elif arr[i] < 0:
                sum = sum + arr[i]
        m.append(a)
        m.append(sum)
        return m
    else:
        return arr