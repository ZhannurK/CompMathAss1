def iteration_method(g, x0, tol, nmax):
    for i in range(nmax):
        x1 = g(x0)

        if abs(x1 - x0) < tol:
            print(f"Root found: {x1} after {i + 1} iterations.")
            return x1

        x0 = x1

    print("Root not found within the given tolerance and maximum iterations.")
    return None

def g(x):
    return (x + 1) ** (1 / 3)

## def g(x): return x ** 3 - x - 1

x0 = 1.5
tol = 1e-7
nmax = 100

root = iteration_method(g, x0, tol, nmax)
print(f"The approximate root is: {root}")