# quadratic equation

def QuadraticEquation():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    d = (b*b)-4*a*c
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
        s0 = -s+(v0*t)+((a*(t*t))/2)  
        return s0

    if s == None:
        s = s0 + (v0*t) + ((a*(t*t))/2)
        return s