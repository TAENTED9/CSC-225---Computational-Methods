from sympy import lambdify
from sympy import symbols, diff

#Define the function and its derivative
x = symbols('x')
f = eval(input("\nNEWTON RAPHSON METHOD\nInput Function: \n"))
dfx = diff(f, x)

# Lambdify the function and its derivative for numerical use
f_x = lambdify(x, f)
f_prime_x = lambdify(x, dfx)

#Since  f(1) < 0 and f(3) > 0,  We shall take this to be 2 by bisection.
x0 = float(input("Enter a starting guess: "))
tol = 1e-7
No_of_iterations = int(input("Enter the number of iterations: "))

# Now you can use f_x(x0) and f_prime_x(x0) for calculations
print("\n  n       |       x       |       f(x)       |       f'(x)       ")
print("-------------------------------------------------------------------")
for i in range(No_of_iterations):
    if dfx == 0:
        raise ValueError("Derivative is zero. No solution found.")
    
    x_new = x0 - (f_x(x0) / f_prime_x(x0))
    print(f"     {i+1:4d} | {x0:10.6f} | {f_x(x0):15.6f} | {f_prime_x(x0):15.6f}")
    
    if abs(x_new - x0) < tol:
        break
    x0 = x_new
print(f"\nRoot found: x = {x0:.6f} after {i+1} iterations.")
