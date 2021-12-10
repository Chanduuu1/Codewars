import math
def is_square(n):  
    if n >= 0:
        a = math.sqrt(n)
        b = int(a)
        if b*b == n:
            return True
        else:
            return False
    else:
        return False 