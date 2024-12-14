def bisection_method(f, a, b, tol, nmax):
    results = [a, b]
    if f(a) * f(b) >= 0:
        raise ValueError("Function must have opposite signs at endpoints a and b.")

    i = 0
    while i <= nmax:
        c = (a + b) / 2
        results.append(c)
        if f(c) == 0 or abs(f(c)) <= tol:
            break

        if f(c) * f(a) > 0:
            a = c
        else:
            b = c

        i += 1
    return results

def secant_method(f, x0, x1, tol, nmax):
    results = [x0, x1]
    for i in range(nmax):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < 1e-12:
            raise ZeroDivisionError("Division by zero encountered.")

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        results.append(x2)

        if abs(x2 - x1) < tol:
            break

        x0 = x1
        x1 = x2
    return results

def iteration_method(g, x0, tol, nmax):
    results = [x0]
    for i in range(nmax):
        x1 = g(x0)
        results.append(x1)

        if abs(x1 - x0) < tol:
            break

        x0 = x1
    return results

def newton_raphson_method(f, df, x0, tol, nmax):
    results = [x0]
    for i in range(nmax):
        h = f(x0) / df(x0)
        x1 = x0 - h
        results.append(x1)

        if abs(h) <= tol:
            break

        x0 = x1
    return results

def construct_table(method1, method2, method3, method4):
    max_length = max(len(method1), len(method2), len(method3), len(method4))

    method1.extend(["..."] * (max_length - len(method1)))
    method2.extend(["..."] * (max_length - len(method2)))
    method3.extend(["..."] * (max_length - len(method3)))
    method4.extend(["..."] * (max_length - len(method4)))

    rows = [
        ["Step", "Bisection", "Secant", "Iteration", "Newton-Raphson"]
    ]
    for i in range(max_length):
        rows.append([i] + [method1[i], method2[i], method3[i], method4[i]])

    table = "\n".join(["\t".join(map(str, row)) for row in rows])
    return table

def f(x):
    return x ** 3 - x - 1

def df(x):
    return 3 * x ** 2 - 1

def g(x):
    return (x + 1) ** (1 / 3)

bisection_results = bisection_method(f, 1, 2, 1e-7, 100)
secant_results = secant_method(f, 1.0, 1.5, 1e-7, 100)
iteration_results = iteration_method(g, 1.5, 1e-7, 100)
newton_results = newton_raphson_method(f, df, 1, 1e-7, 100)

table = construct_table(bisection_results, secant_results, iteration_results, newton_results)
print(table)