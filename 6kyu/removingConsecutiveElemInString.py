l=[]
s = "AAAABBBCCDAABBB"
l1 = list(s)
x = len(l1)
for i in range(1,x):
    a = l1[i-1]
    b = l1[i]
    if a == b:
        l1.pop(i)
        x-=1
    else:
        continue
print(l)
