import numpy as np  # Import numpy for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from scipy.fftpack import fft  # Import FFT function from scipy

# Define constants for the signal
signal_length = 0.5  # Total duration of the signal in seconds
sample_rate = 500  # Number of samples per second (Hz)
dt = 1.0 / sample_rate  # Time interval between samples (seconds)
df = 1.0 / signal_length  # Frequency resolution (Hz)

# Create a time vector from 0 to signal_length with steps of dt
# This represents the time at which each sample is taken
t = np.arange(0, signal_length, dt)
n_t = len(t)  # Total number of time samples

# Create a signal by adding two sine waves of different frequencies and phases
y = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 70 * t + np.pi / 4)

# Compute the Fast Fourier Transform (FFT) of the signal
f = fft(y)

# Generate the frequency vector for plotting the FFT result
# Only take the positive frequencies (first half of FFT result)
freqs = df * np.arange(0, n_t // 2)
n_freq = len(freqs)  # Number of frequency points to plot

# Plot the original signal in the time domain
plt.figure(figsize=(10, 6))  # Set the figure size
plt.subplot(2, 1, 1)  # Create the first subplot (top)
plt.plot(t, y, label='Input Signal')  # Plot signal vs time
plt.xlabel('Time [s]')  # Label for x-axis
plt.ylabel('Amplitude')  # Label for y-axis
plt.title('Time Domain Signal')  # Title for the plot
plt.legend()  # Show legend
plt.grid(True)  # Add grid for better readability

# Plot the magnitude of the FFT (frequency spectrum)
plt.subplot(2, 1, 2)  # Create the second subplot (bottom)
plt.plot(freqs, 2.0 / n_t * np.abs(f[:n_freq]), label='Magnitude Spectrum')
plt.xlabel('Frequency [Hz]')  # Label for x-axis
plt.ylabel('Magnitude')  # Label for y-axis
plt.title('Frequency Domain (FFT)')  # Title for the plot
plt.legend()  # Show legend
plt.grid(True)  # Add grid for better readability

# Save the plot as a PDF file
plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig('fft1.pdf')  # Save the figure to disk
plt.show()  # Display the plot on the screen

# ---
# Summary of what this code does:
# 1. Creates a signal made of two sine waves.
# 2. Computes its FFT to analyze frequency content.
# 3. Plots both the original signal and its frequency spectrum.
# 4. Saves the plot as a PDF and shows it on screen.