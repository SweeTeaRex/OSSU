def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    # quadratic formuala a*x^2+b*x+c
    quad1 = ((a1*x1**2)+(b1**x1)+c1)
    quad2 = ((a2*x2**2)+(b2**x2)+c2)
    return quad1+quad2


print(two_quadratics(1,1,1,1,1,1,1,1))
