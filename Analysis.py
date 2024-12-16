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

def compute_true_root(f, method, *args):
    results = method(f, *args, 1e-12, 1000)
    return results[-1]

def compute_errors(results, true_root):
    final_approx = results[-1]
    absolute_error = abs(final_approx - true_root)
    relative_error = absolute_error / abs(true_root)
    return absolute_error, relative_error

true_root = compute_true_root(f, newton_raphson_method, df, 1)

bisection_results = bisection_method(f, 1, 2, 1e-7, 100)
secant_results = secant_method(f, 1.0, 1.5, 1e-7, 100)
iteration_results = iteration_method(g, 1.5, 1e-7, 100)
newton_results = newton_raphson_method(f, df, 1, 1e-7, 100)

bisection_errors = compute_errors(bisection_results, true_root)
secant_errors = compute_errors(secant_results, true_root)
iteration_errors = compute_errors(iteration_results, true_root)
newton_errors = compute_errors(newton_results, true_root)

print(f"True root: {true_root:.12f}")
print("\nMethod\t\tAbsolute Error\tRelative Error")
print(f"Bisection\t{bisection_errors[0]:.7e}\t{bisection_errors[1]:.7e}")
print(f"Secant\t\t{secant_errors[0]:.7e}\t{secant_errors[1]:.7e}")
print(f"Iteration\t{iteration_errors[0]:.7e}\t{iteration_errors[1]:.7e}")
print(f"Newton-Raphson\t{newton_errors[0]:.7e}\t{newton_errors[1]:.7e}")