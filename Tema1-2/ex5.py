def cmmdc(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

print(cmmdc(120, 27))