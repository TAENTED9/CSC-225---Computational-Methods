from sympy import symbols, lambdify, sympify
from sympy.parsing.sympy_parser import * 

# Define symbols for x and y
x, y = symbols('x y')

# Get initial values and parameters from user
x0 = float(input("Enter the initial value x0: "))
y0 = float(input("Enter the initial value y0: "))
h = float(input("Enter the step size h: "))
deriv_str = input("Enter the function y' as a function of x and y (e.g., x + y): ")
f = parse_expr(deriv_str, transformations = (standard_transformations + (implicit_multiplication_application,)), local_dict={"cos": cos, "sin": sin, "exp": exp, "log": log, "sqrt": sqrt} )
y_prime = sympify(deriv_str)
n_steps = int(input("Enter the number of steps n: "))
target_x = float(input("Enter the target x value xt: "))

# Prepare the function for y'
y_prime_func = lambdify((x, y), y_prime)

# Print table header
print("   Step |     x      |     y     ")
print("---------------------------------")

# Euler's Method Implementation
for step in range(1, n_steps + 1):
    y0 += h * y_prime_func(x0, y0)  # Update y using Euler's formula
    x0 += h                        # Update x
    print(f"  {step:4d} | {x0:8.4f} | {y0:8.4f}")
    if x0 >= target_x:
        break