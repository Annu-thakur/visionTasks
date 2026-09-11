import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Convert image to floating-point format
image_float = np.float32(image)

# Compute 2D DFT
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift the low-frequency components to the center
dft_shifted = np.fft.fftshift(dft)

# Calculate magnitude spectrum
magnitude = cv2.magnitude(
    dft_shifted[:, :, 0],
    dft_shifted[:, :, 1]
)

# Apply logarithmic scaling for visualization
magnitude_spectrum = 20 * np.log(magnitude + 1)

# Display and save the magnitude spectrum
plt.figure(figsize=(8, 6))
plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("Magnitude Spectrum")
plt.axis("off")
plt.savefig("output.png", bbox_inches="tight")
plt.close()

print("Magnitude spectrum saved as output.png")