from sympy import *
from sympy.parsing.sympy_parser import *
import numpy as np
import matplotlib.pyplot as plt 

''' Finding roots using bisection model '''

# Define the function whose root we want to find
x = symbols('x')
print('\nBISECTION METHOD')
user_input = input("\nEnter Function f(x) =  ")
# Parse the user input into a sympy expression
f = parse_expr(user_input, transformations=(standard_transformations + (implicit_multiplication_application,)), local_dict={"cos": cos, "sin": sin, "exp": exp, "log": log, "sqrt": sqrt})

# Convert to a function that can handle numpy arrays
f_x = lambdify(x, f, 'numpy')

# Input interval [a, b]
a, b = float(input('Input the value of a: ')), float(input('Input the value of b: '))

# Check if the initial interval is valid
if f_x(a) * f_x(b) > 0:
    print("\nERROR! f(a) and f(b) must have opposite signs. Choose a different interval [a, b].")
else:
    n = int(input('No of trials (iterations): '))
    tol = float(input('Tolerance (e.g., 1e-6): '))
    print("\nIter |     a      |     b      |     x      |   f(x)   | Interval")
    print("-------------------------------------------------------------------")
    x_lst, y_lst  = [], []
    for p in range(1, n+1):
        x_mid = (a + b) / 2.0
        fx_mid = f_x(x_mid)
        # Store for plotting
        x_lst.append(x_mid)
        y_lst.append(fx_mid)
        print(f"{p:4d} | {a:10.6f} | {b:10.6f} | {x_mid:10.6f} | {fx_mid:9.6f} | {abs(b-a):9.6f}")
        # Check for convergence
        if abs(fx_mid) < tol or abs(b - a) < tol:
            print(f"\nRoot found: x = {x_mid} (f(x) = {fx_mid}) after {p} iterations.")
            break
        # Update the interval based on the sign of f(a) * f(x_mid)
        else:
           if f_x(a) * fx_mid < 0:
                b = x_mid
           else:
                a = x_mid
    else:
        print(f"\nMethod did not converge after {n} iterations. Last x = {x_mid}, f(x) = {fx_mid}")

    # Plot the convergence of the root
    plt.plot(x_lst, y_lst, "ko-", label="Root Convergence")
    plt.xlabel('X-axis (Approximate Roots)')
    plt.ylabel('Y-axis [F(x)]')
    plt.title('Bisection convergence graph')
    plt.legend()
    plt.grid(True)
    plt.show()