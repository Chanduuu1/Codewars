n = int(input())
s = int((n-1)/2)
p = 1
for i in range(0,n,2):
    print(" "*(s) +"*"*(i+1))
    s = s - 1

for j in range(n-2,0,-2):
    print(" "*p + "*"*(j))
    p += 1
