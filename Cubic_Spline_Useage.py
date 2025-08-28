import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# === Cubic Spline Function ===
def my_cubic_spline_flat(x, y, X):
    n = len(x)
    h = np.diff(x)  # h[i] = x[i+1] - x[i]

    A = np.zeros((n, n))
    r = np.zeros(n)

    A[0, 0] = 1
    A[-1, -1] = 1

    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        r[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    c = np.linalg.solve(A, r)
    a = y[:-1]
    b = np.zeros(n - 1)
    d = np.zeros(n - 1)

    for i in range(n - 1):
        b[i] = (y[i + 1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    Y = np.zeros_like(X)
    for j, xj in enumerate(X):
        i = np.searchsorted(x, xj) - 1
        i = max(0, min(i, n - 2))
        dx = xj - x[i]
        Y[j] = a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3

    return Y

# === Sample x and y points ===
x = np.array([0, 1, 2, 3, 4], dtype=float)
y = np.array([0, 1, 0, 1, 0], dtype=float)

# === Interpolation points ===
X_full = np.linspace(x[0], x[-1], 500)
Y_full = my_cubic_spline_flat(x, y, X_full)

# === Interval Indexing for Animation ===
intervals = [(x[i], x[i + 1]) for i in range(len(x) - 1)]
frames = []

for i, (x_start, x_end) in enumerate(intervals):
    mask = (X_full >= x_start) & (X_full <= x_end)
    frames.append((X_full[mask], Y_full[mask]))

# === Set up Plot ===
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-', lw=2)
ax.plot(x, y, 'ro', label='Data points')
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y) - 0.5, np.max(y) + 0.5)
ax.legend()
ax.set_title("Cubic Spline Interpolation Animation")

# === Animation Update Function ===
def update(frame_idx):
    x_interval, y_interval = frames[frame_idx]
    line.set_data(x_interval, y_interval)
    return line,

# === Animate ===
ani = FuncAnimation(fig, update, frames=len(frames), blit=True, interval=700, repeat=True)
plt.show()
