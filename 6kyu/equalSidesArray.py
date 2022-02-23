def find_even_index(arr):
    l = []
    r = []
    sumL = 0
    sumR = 0
    for i in range(0,len(arr)):
        l = arr[0:i]    #Although 1st arr[0:0] = empty list but ho sakta hai 0 index ke right me saare ka sum = exact 0(-ve integer ho toh case possibe) 
                        #And that would be equal to left side of 0 index which again is 0 so test cases ke according
        r = arr[i+1:len(arr)] 
        
        for j in range(len(l)):
            sumL += l[j]
        for k in range(len(r)):
            sumR += r[k]

        if sumL == sumR:
            return i
            break
        
        elif i == len(arr)-1:
            return -1
        
        else:
            sumL = 0
            sumR = 0
            continue

print(find_even_index([1,2,3,4,3,2,1]))


