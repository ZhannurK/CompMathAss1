import matplotlib.pyplot as plt

def bisection_method(f, a, b, tol, nmax):
    results = []
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

def compute_errors(results, true_root):
    return [abs(x - true_root) / abs(true_root) for x in results]

def f(x):
    return x ** 3 - x - 1

def df(x):
    return 3 * x ** 2 - 1

def g(x):
    return (x + 1) ** (1 / 3)

true_root = 1.324718

bisection_results = bisection_method(f, 1, 2, 1e-7, 5)  # First 5 steps
secant_results = secant_method(f, 1.0, 1.5, 1e-7, 5)
iteration_results = iteration_method(g, 1.5, 1e-7, 5)
newton_results = newton_raphson_method(f, df, 1, 1e-7, 5)

bisection_errors = compute_errors(bisection_results, true_root)
secant_errors = compute_errors(secant_results, true_root)
iteration_errors = compute_errors(iteration_results, true_root)
newton_errors = compute_errors(newton_results, true_root)

plt.figure(figsize=(8, 6))
plt.plot(range(len(bisection_errors)), bisection_errors, '-o', label="Bisection Method")
plt.plot(range(len(secant_errors)), secant_errors, '-o', label="Secant Method")
plt.plot(range(len(iteration_errors)), iteration_errors, '-o', label="Iteration Method")
plt.plot(range(len(newton_errors)), newton_errors, '-o', label="Newton-Raphson Method")

plt.title("Relative Error Comparison")
plt.xlabel("Iteration Step")
plt.ylabel("Relative Error")
plt.yscale('log')
plt.legend()
plt.grid()
plt.show()