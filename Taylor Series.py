import numpy as np
import matplotlib.pyplot as plt
import math


x = np.linspace(-np.pi, np.pi, 200)
y = np.zeros(len(x))

labels = ["First Order", "Third Order", "Fifth Order", "Seventh Order"]


plt.figure(figsize = (14, 6))
for n, label in zip(range(4), labels):
    y = y + ((-1) ** n) * (x ** (2*n + 1)) / math.factorial(2*n + 1)
    plt.plot(x, y, label = label)
    

plt.plot(x, np.sin(x), "k", label= "Analytic")
plt.grid()
plt.title("Taylor Series Approximations of Various Orders")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()



#--------------------------------------------------------------------
#Computing Just Seventh Order

x = np.pi / 2
y = 0

for n in range(4):
    y = y + (((-1) ** n ) * (x ** (2*n + 1)) / math.factorial(2*n + 1))

print(y)


#---------------------------------------------------------------------
x =np.linspace(0,3,30)
y =np.exp(x)

plt.figure(figsize=(14, 6))

plt.subplot(1, 3, 1)
plt.plot(x, y)
plt.grid()

plt.subplot(1, 3, 2)
plt.plot(x, y)
plt.grid()
plt.xlim(1.7, 2.3)
plt.ylim(5, 10)

plt.subplot(1, 3, 3)
plt.plot(x, y)
plt.grid()
plt.xlim(1.92, 2.08)
plt.ylim(6.6, 8.2)

plt.tight_layout()
plt.show()
