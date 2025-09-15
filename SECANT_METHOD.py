#Secant Method
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import *


x = symbols('x')
print("\nSecant Method")
user_input = input("Enter Function f(x) = ")
f = parse_expr(user_input, transformations = (standard_transformations + (implicit_multiplication_application,)), local_dict = {"cos": cos, "sin": sin, "x": x})
f_x = lambdify(x, f, 'numpy')


x0, x1 = float(input('Input the value of x0: ')), float(input('Input the value of x1: '))
tol = float(input("Enter tolerance: "))
n = int(input("Enter No of iterations: "))

print("     Xn-1     |     Xn     |     Xn+1     |     f(Xn-1)     |     f(Xn)     |     F(Xn+1)     ")
print("----------------------------------------------------------------------------------------------")
for p in range(1, n):
    x_new = x1 - (f_x(x1) * (x1 - x0)) / (f_x(x1) - f_x(x0))

    print(f"     {x0:.6f}     |     {x1:.6f}     |     {x_new:.6f}     |     {f_x(x0):.6f}     |     {f_x(x1):.6f}     |     {f_x(x_new):.6f}")

    if abs(x1 - x0) < tol:
        print(f"\nThe Root of the Function is x = {x_new} at f(x) = {f_x(x_new)}")
        break
    else:
        temp = x1
        x0 = temp
        x1 = x_new
else:
    print(f"\nNo convergence at iteration {p}. Last value at x = {x_new}")