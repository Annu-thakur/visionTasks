import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Convert image to float32 for DFT computation
image_float = np.float32(image)

# Compute the 2D DFT using OpenCV
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift the frequency representation
shifted_dft = np.fft.fftshift(dft)

# Print the required shapes
print("Original Image Shape:", image.shape)
print("DFT Result Shape:", dft.shape)
print("Shifted DFT Shape:", shifted_dft.shape)

# Create a magnitude image for saving the result
magnitude = cv2.magnitude(
    shifted_dft[:, :, 0],
    shifted_dft[:, :, 1]
)

# Log scaling for visualization
magnitude = np.log(magnitude + 1)

# Normalize to 0-255
magnitude = cv2.normalize(
    magnitude, None, 0, 255, cv2.NORM_MINMAX
)

magnitude = np.uint8(magnitude)

# Save the result
cv2.imwrite("output.png", magnitude)

print("DFT result saved as output.png")