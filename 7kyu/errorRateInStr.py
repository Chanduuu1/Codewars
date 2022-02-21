def printer_error(s):
    l = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    a = 0
    for i in range(len(s)):
        if s[i] not in l:
            a += 1
        else:
            continue
    ans = (f"{a}/{len(s)}")
    return ans