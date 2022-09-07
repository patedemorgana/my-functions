# quadratic equation

def QuadraticEquation(a, b, c):
    d = (b*b)-4*a*c
    x1 = (-b - d)/(2*a)
    x2 = (-b + d)/(2*a)
    print('Δ: ', d)
    print('x1:', x1, '\nx2:',  x2)

