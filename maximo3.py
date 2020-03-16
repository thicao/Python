def maximo(n1, n2, n3):
    max = maior(n1, n2)
    max = maior(max, n3)
    return max

def maior(x, y):
    if x > y:
        return x
    else:
        return y
