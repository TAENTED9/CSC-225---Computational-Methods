from sympy import lambdify  # Import lambdify to convert symbolic expressions to functions
from sympy import symbols, diff 
from sympy.parsing.sympy_parser import * # Import symbols for variable definition and diff for differentiation

# Define the function and its derivative
x = symbols('x')  # Define the symbol x for symbolic computation
print("\nNewton Raphson Method")  # Print method name
user_input = input("\nEnter Function f(x) = ")
f = parse_expr(user_input, transformations=(standard_transformations + (implicit_multiplication_application,)), local_dict={"cos": cos, "sin": sin, "exp": exp, "log": log, "sqrt": sqrt})  # Get the function from user input

dfx = diff(f, x)  # Compute the derivative of the function with respect to x

# Lambdify the function and its derivative for numerical use
f_x = lambdify(x, f, "numpy")  # Convert the symbolic function to a numerical function
f_prime_x = lambdify(x, dfx, "numpy")  # Convert the symbolic derivative to a numerical function

# Input the initial guess and other parameters
x0 = float(input("Enter a starting guess: "))  # Get initial guess from user
tol = float(input('Tolerance (e.g., 1e-6): '))  # Set the tolerance for convergence
No_of_iterations = int(input("Enter the number of iterations: "))  # Get number of iterations from user

print("\n  n       |       x       |       f(x)       |       f'(x)       ")  # Print table header
print("-------------------------------------------------------------------")  # Print table separator
for i in range(No_of_iterations):  # Loop for the specified number of iterations
    # Check if the numerical derivative is zero at the current guess
    if f_prime_x(x0) == 0:
        raise ValueError(f"Derivative is zero at x = {x0}. No solution found.")
    x_new = x0 - (f_x(x0) / f_prime_x(x0))  # Newton-Raphson formula to update x
    print(f"     {i+1:4d} | {x0:10.6f} | {f_x(x0):15.6f} | {f_prime_x(x0):15.6f}")  # Print current iteration values
    if abs(x_new - x0) < tol:  # Check for convergence
        print(f"\nRoot found: x = {x_new:.6f} after {i+1} iterations.")  # Print the found root and number of iterations
        break  # Exit loop if converged
    x0 = x_new  # Update x0 for next iteration
else:
    print(f"\nMethod did not converge after {No_of_iterations} iterations. Last x = {x0:.6f}, f(x) = {f_x(x0):.6f}")