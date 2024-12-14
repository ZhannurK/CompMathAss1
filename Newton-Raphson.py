def newton_raphson(f, df, x0, aerr, maxitr):
    itr = 0
    while itr <= maxitr:
        h = f(x0) / df(x0)
        x1 = x0 - h
        if abs(h) <= aerr:
            print(f"Root found: {x1}")
            return x1
        x0 = x1
        itr += 1
    print("Solution does not converge within the given tolerance and maximum iterations.")
    return None

def f(x):
    return x ** 3 - x - 1

def df(x):
    return 3 * x ** 2 - 1

x0 = 1
aerr = 1e-7
maxitr = 100

root = newton_raphson(f, df, x0, aerr, maxitr)
print(f"The approximate root is: {root}")