# Instruction call anySub.subtract(number1,number2,base)
def compare(f, s):
    if len(f) == 0 and len(s) == 0:
        return 0
    elif f[0] > s[0]:
        return 1
    elif f[0] < s[0]:
        return 1
    else:
        return compare(f[1:], s[1:])


def subtract(x, y, base=2):
    x = str(x)
    y = str(y)
    c = 0
    R = ""
    v = "0123456789ABCDEF"
    while len(x) != len(y):
        if len(x) > len(y):
            s = "0" + s
        if len(x) < len(y):
            f = "0" + f
    p = compare(x, y)
    if p == 1:
        x, y = y, x

    for i in range(len(x) - 1, -1, -1):
        a = c + v.find(x[i])
        b = v.find(y[i])
        if b > a:
            c = -1
            a = a + base
        else:
            c = 0
        R = v[a - b] + R
    return R
