def maskify(cc):
    if len(cc) > 4:
        x = len(cc) - 4
        return "#" * x + cc[x::]
    else:
        return cc