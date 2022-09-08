#Karatsuba

def k(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        h = n // 2
        a = x // (10 ** (h))  
        b = x % (10 ** (h))  
        c = y // (10 ** (h))  
        d = y % (10 ** (h))  
        ac = k(a, c)
        bd = k(b, d)
        ad_plus_bc = k(a+b, c+d)-ac-bd
        return ac * (10 ** (2 * h)) + (ad_plus_bc * (10 ** h)) + bd



def newton_method(func, funcderiv, x, n):
    def f(x):
        f = eval(func)
        return f
    def df(x):
        df = eval(funcderiv)
        return df
    for i in range(1, n):
        i = x - (f(x)/df(x))
        x = i
    print(f"the root {x}, iterations: {n}")





def sqrt(n):
    n ** 0.5
    return n


def QuadraticEquation():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    d = sqrt((b**2)-4*a*c)
    x1 = (-b - d)/(2*a)
    x2 = (-b + d)/(2*a)
    print('x1: ', x1, '\nx2:', x2, '\nΔ:', d)
    return x1, x2, d


def Accel():
    v = int(input('v0: '))
    v0 = int(input('s0: '))
    t = int(input('s0: '))
    t0 = int(input('s0: '))
    a = (v - v0)/(t - t0)
    return a

def MUV():
    s0 = int(input('s0: '))
    v0 = int(input('v0: '))
    t = int(input('t: '))
    a = int(input('a: '))
    s = int(input('s: '))
    if s0 == None:
        s0 = -s+(v0*t)+((a*(t**2))/2)  
        return s0

    if s == None:
        s = s0 + (v0*t) + ((a*(t**2))/2)
        return s