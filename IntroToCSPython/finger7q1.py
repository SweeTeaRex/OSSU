def eval_quadratic(a, b, c, x):
    #quadratic equation is (a*x^2+b*x+c)
    aVar = a*x**2
    bVar = b*x
    return aVar+bVar+c

print(eval_quadratic(1, 1, 1, 1))