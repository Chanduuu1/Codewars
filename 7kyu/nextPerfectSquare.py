# if a given number is a perfect square then return the next perfext square else return -1
import math
def perfSq(n):
    rt = math.sqrt(n)
    if math.ceil(rt) == math.floor(rt):
        return (rt+1) * (rt+1)
    else:
        return -1
print(perfSq(24))

#alternate solution
'''if rt*rt ka int == n mtlb perfect square'''
def perfSq2(m):
    rt = int(math.sqrt(m))
    if rt*rt == m:
        return (rt+1) * (rt+1)
    else:
        return -1
print(perfSq2(25))