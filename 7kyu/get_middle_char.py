def get_middle(s):
    l=len(s)
    if l%2!=0:
        a=int((l+1)/2)
        b=s[a-1]
        return b
    else:
        a=int(l/2)
        b=s[a-1]
        c=s[a]
        d=b+c
        return d