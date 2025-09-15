from sympy import lambdify, symbols

x = symbols('x')
f = eval(input("\nEnter the function f(x): "))
f_x = lambdify(x, f)

# Ask user for initial guess
try:
    x0 = float(input("Enter the initial guess x0: "))
except Exception:
    print("Invalid input for x0. Using x0 = 0.5 as default.")
    x0 = 0.5

n = int(input("Enter the number of iterations: "))
fp = int(input("Enter the number of decimal places for convergence: "))

for i in range(n):
    x1 = f_x(x0)
    print(f"Iteration {i+1}: x0 = {x0}, f(x0) = {x1}")

    if round(x1, fp) == round(x0, fp):
        print(f"Root found: x = {x1} after {i+1} iterations.")
        break
    x0 = x1
else:
    print(f"Did not converge to a root after {n} iterations. Last approximation: x = {x1}")

