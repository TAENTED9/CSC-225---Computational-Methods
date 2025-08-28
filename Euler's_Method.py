from sympy import symbols, lambdify


x = symbols('x')
y = symbols('y')
y0 = eval(input("\nEnter the initial value y0: "))
x0 = eval(input("Enter the initial value x0: "))
h = float(input("Enter the step size h: "))
y_prime = eval(input("Enter the function y' as a function of x and y: "))
ni = 0
i = 0
nf = int(input("Enter the number of steps n: "))
xt = eval(input("Enter the target x value xt: \n"))


# Euler's Method Implementation
print("     n   |      Xn     |    Yn      ")
print("------------------------------------")
while (x0 < xt) or (nf < ni):
    y_prime_func = lambdify((x, y), y_prime)
    y0 += h * y_prime_func(x0, y0)
    x0 += h
    i += 1
    ni += 1
    print(f" {i + 1}|   x = {x0}  |  y = {y0}  ")