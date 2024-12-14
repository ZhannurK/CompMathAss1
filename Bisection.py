import math

def bisection(f, a, b, tol, nmax):
    if f(a) * f(b) >= 0:
        print("Error: The function must have opposite signs at the endpoints a and b.")
        return None

    i = 0
    while i <= nmax:
        c = (a + b) / 2
        if f(c) == 0 or abs(f(c)) <= tol:
            print(f"Root found: {c} after {i} iterations.")
            return c

        if f(c) * f(a) > 0:
            a = c
        else:
            b = c

        i += 1

    print("Root not found within the given tolerance and maximum iterations.")
    return None

def f(x):
    return math.exp(x) - x ** 2

a = 0
b = 2
tol = 1e-7
nmax = 100

root = bisection(f, a, b, tol, nmax)
if root is not None:
    print(f"The approximate root is: {root}")