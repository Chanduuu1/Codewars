def encode(st):
    for i in range(0,len(st)):
        if st[i] == "a":
            st = st[0:i] + "1" + st[i+1:len(st)]
        if st[i] == "e":
            st = st[0:i] + "2" + st[i+1:len(st)]
        if st[i] == "i":
            st = st[0:i] + "3" + st[i+1:len(st)]
        if st[i] == "o":
            st = st[0:i] + "4" + st[i+1:len(st)]
        if st[i] == "u":
            st = st[0:i] + "5" + st[i+1:len(st)]
    return st
    
def decode(st):
    for i in range(0,len(st)):
        if st[i] == "1":
            st = st[0:i] + "a" + st[i+1:len(st)]
        if st[i] == "2":
            st = st[0:i] + "e" + st[i+1:len(st)]
        if st[i] == "3":
            st = st[0:i] + "i" + st[i+1:len(st)]
        if st[i] == "4":
            st = st[0:i] + "o" + st[i+1:len(st)]
        if st[i] == "5":
            st = st[0:i] + "u" + st[i+1:len(st)]
    return st

#Another approch would be using makeTrans() or  translate() function, keep in mind
#Yet anoter approch using replace("jisse replace karna hai","jiss se replace karna hai")