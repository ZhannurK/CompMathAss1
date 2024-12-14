def secant_method(f, x0, x1, tol, nmax):
    for i in range(nmax):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < 1e-12:
            print("Division by zero encountered.")
            return None

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tol:
            print(f"Root found: {x2}")
            return x2

        x0 = x1
        x1 = x2

    print("Root not found within the given tolerance and maximum iterations.")
    return None

def f(x):
    return x ** 3 - x - 1

x0 = 1.0
x1 = 1.5
tol = 1e-7
nmax = 100

root = secant_method(f, x0, x1, tol, nmax)
print(f"The approximate root is: {root}")