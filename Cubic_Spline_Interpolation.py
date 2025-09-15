import numpy as np
import matplotlib.pyplot as plt

# This class does cubic spline interpolation
class Cubic_Spline_Interpolation:

    @staticmethod
    def my_cubic_spline_flat(x, y, X):
        n = len(x)  # Number of data points
        h = np.diff(x)  # Distance between each x value
    
        # Step 1: Build the matrix A*c = r for the system of equations
        A = np.zeros((n, n))  # Matrix for the equation
        r = np.zeros(n)       # a column of the equation

        A[0, 0] = 1  # Set first equation for natural spline (second derivative at start = 0)/ the first element of the matrix
        A[-1, -1] = 1  # Set last equation for natural spline (second derivative at end = 0)/ the last element of the matrix

        # Fill in the rest of the matrix and right side
        for i in range(1, n - 1):
            A[i, i - 1] = h[i - 1]  # Value to the left
            A[i, i] = 2 * (h[i - 1] + h[i])  # Middle value
            A[i, i + 1] = h[i]  # Value to the right
            # Calculate the right side value
            r[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

        # Step 2: Solve for c (second derivatives at each point)
        c = np.linalg.solve(A, r)

        # Step 3: Calculate a, b, d for the spline formula
        a = y[:-1]  # a is just the y values except the last one
        b = np.zeros(n - 1)  # b will be calculated
        d = np.zeros(n - 1)  # d will be calculated

        for i in range(n - 1):
            # Calculate b and d for each interval
            b[i] = (y[i + 1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
            d[i] = (c[i + 1] - c[i]) / (3 * h[i])

        # Step 4: Interpolate each value in X
        X = np.atleast_1d(X)  # Make sure X is an array
        Y = np.zeros_like(X, dtype=float)  # Prepare output array
        for j, xj in enumerate(X):
            # Find which interval xj is in
            i = np.searchsorted(x, xj) - 1
            i = max(0, min(i, n - 2))  # Make sure i is in a valid range

            dx = xj - x[i]  # Distance from left endpoint
            # Calculate the spline value using the formula
            Y[j] = a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3

        return Y
    
if __name__ == "__main__":
    # Example x and y data points
    x = [0., 0.2, 0.4, 0.6, 0.8, 1., 1.2, 1.4, 1.6, 1.8, 2., 2.2, 2.4, 2.6, 2.8]
    y = [10. , 11.216, 11.728, 11.632, 11.024, 10. , 8.656, 7.088, 5.392, 3.664, 2. , 0.496, -0.752, -1.648, -2.096]

    # Test for a single value
    result = Cubic_Spline_Interpolation.my_cubic_spline_flat(x, y, X=1)
    print("Spline at X=1:", result[0])  # Print the result for X=1

    # Test for a range of values and plot
    X_test = np.linspace(min(x), max(x), 200)  # Make 200 points between min and max x
    Y_test = Cubic_Spline_Interpolation.my_cubic_spline_flat(x, y, X_test)  # Get spline values
    plt.plot(x, y, 'o', label='Data Points')  # Plot the original data points
    plt.plot(X_test, Y_test, '-', label='Cubic Spline')  # Plot the spline curve
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cubic Spline Interpolation')
    plt.show()  # Show the plot


