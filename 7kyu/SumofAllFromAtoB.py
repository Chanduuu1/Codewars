def get_sum(a,b):
    sum = 0
    if b > a:
        for i in range(a,b+1):
            sum += i
        return sum
    elif a > b:
        for i in range(b,a+1):
            sum += i
        return sum
    elif a == b:
        return a

print(get_sum(b=2,a=3))