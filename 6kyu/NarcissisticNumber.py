import math
def narcissistic( value ):
    s = str(value)
    n = len(s)
    sum = 0
    for i in s:
        a = int(i)
        sum += math.pow(a,n)  
    if sum == value:
        return True
    else:
        return False
    
    